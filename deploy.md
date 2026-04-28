# Guia de Deploy e Sincronização de Dados - Repositório TCCE

Este documento descreve o estado atual do banco de dados e os procedimentos necessários para realizar o deploy e a carga inicial de dados.

## 📊 Estado Atual
- **Total de Registros:** 454 (importados do arquivo JSON).
- **Integridade:** O banco foi higienizado e as sequências de ID (`sequences`) foram sincronizadas.
- **Duplicidade:** O sistema está configurado para permitir títulos duplicados (conforme solicitado para manter fidelidade ao arquivo de origem).

## 🛠 Procedimentos Pré-Deploy

### 1. Aplicação de Migrations
Garante que a estrutura do PostgreSQL esteja alinhada com os modelos:
```bash
python manage.py migrate
```

### 2. Carga Inicial (Lookups)
Antes de rodar a importação dos registros, é obrigatório popular as tabelas de suporte (Projetos, Áreas, Status, etc.):
```bash
psql -h <host> -U <user> -d <dbname> -f ./www/sql/carga_inicial.sql
```

### 3. Sincronização de IDs (Crucial)
Como os dados iniciais são inseridos via SQL, é necessário resetar os contadores de ID do Django para evitar erros de chave duplicada:
```bash
python manage.py sqlsequencereset apps.repositorio | python manage.py dbshell
```

## 📥 Scripts de Importação
Os scripts estão localizados em `www/django_code/`:

1. **`carga_json.json`**: Contém os 454 itens brutos.
2. **`carga_publicacaoes.py`**: Script que realiza a leitura do JSON e cria os objetos no Django.
   - **Nota:** O script utiliza `Registro.objects.create()` para garantir que todos os 454 itens sejam inseridos, mesmo que haja títulos repetidos.
3. **`achar_duplicatas.py`**: Utilitário para auditoria de registros repetidos no arquivo de origem.

## 📂 Arquivos de Mídia
Os registros apontam para arquivos PDF. Certifique-se de que o diretório `media/` (ou o bucket S3 de produção) contenha os arquivos referenciados no campo `arquivo` do banco.

## 🔑 Auditoria
O script de carga exige um superusuário ativo para assinar os campos de `usuario_criacao`. Se o banco de produção estiver vazio, crie o usuário primeiro:
```bash
python manage.py createsuperuser
```

---
**Desenvolvido por:** João Pedro A. Loiola

**Data:** 28/04/2026





