import os
import sys
from datetime import datetime
import json
from django.db import transaction
from django.db.models import ObjectDoesNotExist
from django.contrib.auth import get_user_model

# --------------------------------------------------------------------------------
# 1. CONFIGURAÇÃO DO AMBIENTE DJANGO
# --------------------------------------------------------------------------------

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
# Ajuste conforme sua estrutura
BASE_DIR = os.path.abspath(os.path.join(CURRENT_DIR, '..', '..')) 
JSON_FILE_PATH = os.path.join(CURRENT_DIR, 'carga_json.json')

sys.path.insert(0, BASE_DIR)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "repositoriotcce.settings")

import django
django.setup()

# --------------------------------------------------------------------------------
# 2. IMPORTAÇÃO DOS MODELOS
# --------------------------------------------------------------------------------
from apps.repositorio.models import (
    Registro, Projeto, Subprojeto, Autor, Tag,
    TipoDocumento, AreaTematica, Status, TipoPublicacao
)
User = get_user_model()

# --------------------------------------------------------------------------------
# 3. FUNÇÃO PRINCIPAL DE IMPORTAÇÃO
# --------------------------------------------------------------------------------

def run_import():
    registros_criados_count = 0
    registros_existentes_count = 0
    registros_duplicados_count = 0
    erros = []

    # Leitura do JSON
    if not os.path.exists(JSON_FILE_PATH):
        print(f"ERRO: Arquivo {JSON_FILE_PATH} não encontrado!")
        return

    try:
        with open(JSON_FILE_PATH, 'r', encoding='utf-8') as f:
            itens_para_importar = json.load(f)
    except Exception as e:
        print(f"ERRO ao ler o JSON: {e}")
        return

    # Obter usuário para auditoria
    auditor_user = User.objects.filter(is_superuser=True, is_active=True).first() or User.objects.first()
    if not auditor_user:
        print("ERRO CRÍTICO: Nenhum usuário encontrado no banco.")
        return

    print(f"Usuário de Auditoria: {auditor_user.email}")
    print(f"Total de itens a importar: {len(itens_para_importar)}")

    try:
        with transaction.atomic():
            for i, item_data in enumerate(itens_para_importar):
                try:
                    # --- A. Busca de FKs ---
                    projeto = Projeto.objects.get(nome=item_data["PROJETO"])
                    
                    # Subprojeto (get_or_create retorna tupla)
                    sub_obj, created_sub = Subprojeto.objects.get_or_create(
                        projeto=projeto,
                        nome=item_data["SUBPROJETO"]
                    )

                    tipo_documento = TipoDocumento.objects.get(nome=item_data["TIPO_DOCUMENTO"])
                    area_tematica = AreaTematica.objects.get(nome=item_data["AREA_TEMATICA"])
                    status = Status.objects.get(nome=item_data["STATUS"])
                    tipo_publicacao = TipoPublicacao.objects.get(nome=item_data["TIPO_PUBLICACAO"])

                    # Data
                    data_str = item_data.get("DATA", "")
                    data_publicacao = None
                    if data_str and '/' in data_str:
                        try:
                            data_publicacao = datetime.strptime(f'01/{data_str}', '%d/%m/%Y').date()
                        except: pass

                    # Lógica de Arquivo vs Link
                    link_real = (item_data.get("LINK_REAL") or "").strip()
                    arquivo_valor = None
                    link_externo_valor = None

                    if "LINK" in tipo_publicacao.nome.upper() or link_real.startswith("http"):
                        link_externo_valor = link_real
                    else:
                        arquivo_valor = link_real if link_real.lower().endswith(".pdf") else f"{link_real}.pdf"

                    # --- B. Criação/Atualização do Registro ---
                    registro, created = Registro.objects.update_or_create(
                        subprojeto=sub_obj,
                        tipo_documento=tipo_documento,
                        titulo=item_data["TITULO"],
                        defaults={
                            'area_tematica': area_tematica,
                            'status': status,
                            'tipo_publicacao': tipo_publicacao,
                            'data_publicacao': data_publicacao,
                            'arquivo': arquivo_valor,
                            'link_externo': link_externo_valor,
                            'usuario_criacao': auditor_user,
                            'usuario_ultima_atualizacao': auditor_user,
                            'ativo': True,
                        }
                    )

                    if created: registros_criados_count += 1
                    else: registros_existentes_count += 1

                    # --- C. M2M (Autores e Tags) ---
                    # Autores
                    autores_names = [a.strip() for a in item_data.get("AUTOR", "").split(',') if a.strip()]
                    for nome in autores_names:
                        autor = Autor.objects.filter(nome=nome).first()
                        if autor: registro.autores.add(autor)

                    # Tags
                    tags_names = [t.strip().replace(',', '').replace('.', '') for t in item_data.get("TAGS", "").split(';') if t.strip()]
                    for t_nome in tags_names:
                        tag = Tag.objects.filter(nome=t_nome).first()
                        if tag: registro.tags.add(tag)

                    print(f"Progresso: {i+1}/{len(itens_para_importar)} - {registro.titulo[:30]}...")

                except Exception as e:
                    print(f"Erro no item {i}: {e}")
                    raise # Força rollback do atomic

        print("\n--- RESULTADO FINAL ---")
        print(f"Criados: {registros_criados_count} | Atualizados: {registros_existentes_count}")

    except Exception as e:
        print(f"\nImportação abortada: erro detectado (Rollback executado). Erro: {e}")

if __name__ == "__main__":
    run_import()