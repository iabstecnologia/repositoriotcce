import os
import sys
from datetime import datetime
from decimal import Decimal
import re
from django.db import transaction
from django.db.models import ObjectDoesNotExist
from django.contrib.auth import get_user_model

# --------------------------------------------------------------------------------
# 1. CONFIGURAÇÃO DO AMBIENTE DJANGO (CRÍTICO)
# --------------------------------------------------------------------------------

# 1. Determina o caminho absoluto do diretório 'backend/'
# O script está em: backend/config/script/django/
# Subir 4 níveis: /django -> /script -> /config -> /backend/
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
BACKEND_DIR = os.path.abspath(os.path.join(CURRENT_DIR, 'backend'))

# 2. Adiciona o diretório 'backend/' ao sys.path.
# Isso permite que o Python encontre os módulos 'config' e 'apps'.
sys.path.insert(0, BACKEND_DIR)

# 3. Define o módulo de settings.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "repositoriotcce.settings")

import django

try:
    # Garante que o Django inicialize o ambiente.
    django.setup()
except Exception as e:
    print(f"Erro ao configurar o Django (Verifique DJANGO_SETTINGS_MODULE): {e}")
    sys.exit(1)

# --------------------------------------------------------------------------------
# 2. IMPORTAÇÃO DOS MODELOS
# --------------------------------------------------------------------------------
try:
    # As importações de apps.repositorio agora devem funcionar
    from apps.repositorio.models import (
        Registro, Projeto, Subprojeto, Autor, Tag,
        TipoDocumento, AreaTematica, Status, TipoPublicacao
    )

    User = get_user_model()
except Exception as e:
    print(f"Erro ao importar modelos do Repositorio: {e}.")
    sys.exit(1)

# --------------------------------------------------------------------------------
# 3. DADOS PARA INSERÇÃO (LISTA DE DICIONÁRIOS)
# --------------------------------------------------------------------------------

ITENS = [
    {
        "PROJETO": "TCCE 1/2018", "SUBPROJETO": "SUBPROJETO 2", "AUTOR": "DIEGO DE MEDEIROS BENTO",
        "TITULO": "FILOGEOGRAFIA DE INVERTEBRADOS CAVERNÍCOLAS EM FORMAÇÕES FERRÍFERAS E CARBONÁTICAS - EVOLUÇÃO E CONECTIVIDADE BIOLÓGICA EM AMBIENTES SUBTERRÂNEOS COMO DEFINIDORES DE AÇÕES DE CONSERVAÇÃO",
        "DATA": "09/2024", "TIPO_DOCUMENTO": "RELATÓRIO TÉCNICO FINAL", "AREA_TEMATICA": "MEIO BIÓTICO",
        "STATUS": "PRODUZIDO", "TIPO_PUBLICACAO": "ARQUIVO PDF",
        "LINK_REAL": "SUBPROJETO_2_(DIEGO_MEDEIROS)_FILOGEOGRAFIA_DE_INVERTEBRADOS",
        "TAGS": "FILOGEOGRAFIA; INVERTEBRADOS; EVOLUÇÃO; CONSERVAÇÃO"
    },
    {
        "PROJETO": "TCCE 1/2018", "SUBPROJETO": "SUBPROJETO 4.1", "AUTOR": "ENRICO BERNARD, NARJARA TÉRCIA PIMENTAL",
        "TITULO": "MONITORAMENTO TÉRMICO DE BAT CAVES NA FLORESTA NACIONAL DE CARAJÁS, SERRA NORTE - PARAUAPEBAS/PA",
        "DATA": "06/2023", "TIPO_DOCUMENTO": "RELATÓRIO TÉCNICO FINAL", "AREA_TEMATICA": "MEIO BIÓTICO",
        "STATUS": "PRODUZIDO", "TIPO_PUBLICACAO": "ARQUIVO PDF",
        "LINK_REAL": "SUBPROJETO_4.1_(ENRICO_BERNARD)_MONITORAMENTO_TÉRMICO",
        "TAGS": "BAT CAVES; TÉRMICO; FERRÍFERAS; CARAJÁS; EDITAL"
    },
    {
        "PROJETO": "TCCE 1/2018", "SUBPROJETO": "SUBPROJETO 4.2", "AUTOR": "MARIA ELINA BICHUETTE",
        "TITULO": "ASSOCIAÇÃO DE MORCEGOS (MAMMALIA, CHIROPTERA) A CAVIDADES FERRÍFERAS ATRAVÉS DE LEVANTAMENTO SIMPLES - A IMPORTÂNCIA DAS AICOM's e SICOM's",
        "DATA": "12/2023", "TIPO_DOCUMENTO": "RELATÓRIO TÉCNICO FINAL", "AREA_TEMATICA": "MEIO BIÓTICO",
        "STATUS": "PRODUZIDO", "TIPO_PUBLICACAO": "ARQUIVO PDF",
        "LINK_REAL": "SUBPROJETO_4.2_(MARIA_ELINA)_ASSOCIAÇÃO_DE_MORCEGOS",
        "TAGS": "MORCEGOS; CHIROPTERA; FERRÍFERAS; CARAJÁS; EDITAL"
    },
    {
        "PROJETO": "TCCE 1/2018", "SUBPROJETO": "SUBPROJETO 4.3", "AUTOR": "ADRIANA MARIA COIMBRA HORBE",
        "TITULO": "GEOQUÍMICA E ISÓTOPOS APLICADOS AO ESTUDO GEOECOLÓGICO DAS CAVERNAS DA REGIÃO DE CARAJÁS",
        "DATA": "10/2023", "TIPO_DOCUMENTO": "RELATÓRIO TÉCNICO FINAL", "AREA_TEMATICA": "MEIO FÍSICO",
        "STATUS": "PRODUZIDO", "TIPO_PUBLICACAO": "ARQUIVO PDF",
        "LINK_REAL": "SUBPROJETO_4.3_(ADRIANA_HORBE)_GEOQUÍMICA_E_ISÓTOPOS",
        "TAGS": "GEOQUÍMICA; ISÓTOPOS; GEOECOLOGIA; FERRÍFERAS; CARAJÁS; EDITAL"
    },
    {
        "PROJETO": "TCCE 1/2018", "SUBPROJETO": "SUBPROJETO 4.4", "AUTOR": "JULIO CESAR PIECZARKA",
        "TITULO": "MORCEGOS DE CAVERNAS: CONHECER PARA PRESERVAR. DIVERSIDADE GENÉTICA, BANCO DE CÉLULAS E DE TECIDOS",
        "DATA": "10/2023", "TIPO_DOCUMENTO": "RELATÓRIO TÉCNICO FINAL", "AREA_TEMATICA": "MEIO BIÓTICO",
        "STATUS": "PRODUZIDO", "TIPO_PUBLICACAO": "ARQUIVO PDF",
        "LINK_REAL": "SUBPROJETO_4.4_(JULIO_CESAR)_MORCEGOS_DE_CAVERNAS",
        "TAGS": "MORCEGOS; CHIROPTERA; FERRÍFERAS; CARAJÁS; EDITAL"
    },
    {
        "PROJETO": "TCCE 1/2018", "SUBPROJETO": "SUBPROJETO 4.5", "AUTOR": "JONAS EDUARDO GALLÃO",
        "TITULO": "DIVERSIDADE DE ARTHROPODA EM CAVIDADES FA FLORESTA NACIONAL DE CARAJÁS E PARQUE NACIONA DOS CAMPOS FERRUGINOSOS - O HABITAT SUBTERRÂNEO, A CONECTIVIDADE ENTRE SUAS POPULAÇÕES E A INFLUÊNCIA DO ENTORNO",
        "DATA": "04/2024", "TIPO_DOCUMENTO": "RELATÓRIO TÉCNICO FINAL", "AREA_TEMATICA": "MEIO BIÓTICO",
        "STATUS": "PRODUZIDO", "TIPO_PUBLICACAO": "ARQUIVO PDF",
        "LINK_REAL": "SUBPROJETO_4.5_(JONAS_GALLÃO)_DIVERSIDADE_DE_ARTHROPODA",
        "TAGS": "ARTHROPODA; FERRÍFERAS; CARAJÁS; EDITAL"
    },
    {
        "PROJETO": "TCCE 1/2018", "SUBPROJETO": "SUBPROJETO 5.1", "AUTOR": "ALEXANDRE BONESSO SAMPAIO",
        "TITULO": "RESTAURAÇÃO ECOLÓGICA DE ÁREAS DEGRADADAS NO ENTRONO DE CAVIDADES NATURAIS NA APA NASCENTES DO RIO VERMELHO, GO",
        "DATA": "08/2025", "TIPO_DOCUMENTO": "RELATÓRIO TÉCNICO FINAL", "AREA_TEMATICA": "OUTROS",
        "STATUS": "PRODUZIDO", "TIPO_PUBLICACAO": "ARQUIVO PDF",
        "LINK_REAL": "SUBPROJETO_5.1_(ALEXANDRE_SAMPAIO)_RESTAURAÇÃO_ECOLÓGICA",
        "TAGS": "RESTAURAÇÃO; ECOLOGIA; PASTAGEM; APANRV"
    },
    {
        "PROJETO": "TCCE 1/2018", "SUBPROJETO": "SUBPROJETO 5.2", "AUTOR": "ROGERIO UAGODA",
        "TITULO": "SUSCEPTIBILIDADE, HIDROLOGIA E GEOMORFOLOGIA CÁRSTICA APLICADAS À CONSERVAÇÃO DO PATRIMÔNIO ESPELEOLÓGICO DA ÁREA DE PROTAÇÃO AMBIENTAL DAS NASCENTES DO RIO VERMELHO",
        "DATA": "08/2023", "TIPO_DOCUMENTO": "RELATÓRIO TÉCNICO FINAL", "AREA_TEMATICA": "MEIO FÍSICO",
        "STATUS": "PRODUZIDO", "TIPO_PUBLICACAO": "ARQUIVO PDF",
        "LINK_REAL": "SUBPROJETO_5.2_(ROGÉRIO_UAGODA)_HIDROLOGIA",
        "TAGS": "HIDROLOGIA; GOMORFOLOGIA; CARSTE; APANRV"
    },
    {
        "PROJETO": "TCCE 1/2018", "SUBPROJETO": "SUBPROJETO 6",
        "AUTOR": "ÉZIO LUIZ RUBBIOLI, AUGUSTO SARREIRO AULER, MARIA ELINA BICHUETTE, ANDRÉ GOMIDE VASCONCELOS",
        "TITULO": "ESTUDOS PARA DEFINIÇÃO DE ÁREAS PRIORITÁRIAS PARA A CONSERVAÇÃO DO PATRIMÔNIO ESPELEOLÓGICO NA SERRA DO RAMALHO, BA",
        "DATA": "11/2024", "TIPO_DOCUMENTO": "RELATÓRIO TÉCNICO FINAL", "AREA_TEMATICA": "OUTROS",
        "STATUS": "PRODUZIDO", "TIPO_PUBLICACAO": "ARQUIVO PDF",
        "LINK_REAL": "SUBPROJETO_6_(ÉZIO_RUBIOLLI)_ESTUDOS_PARA_DEFINIÇÃO",
        "TAGS": "CONSERVAÇÃO; PRIORITÁRIA; PATRIMÔNIO"
    },
    {
        "PROJETO": "TCCE 1/2018", "SUBPROJETO": "SUBPROJETO 7", "AUTOR": "FLÁVIO SILVA RAMOS",
        "TITULO": "SISTEMA DE CADASTRO NACIONAL DE INFORMAÇÕES ESPELEOLÓGICAS (CANIE)",
        "DATA": "05/2024", "TIPO_DOCUMENTO": "RELATÓRIO TÉCNICO FINAL", "AREA_TEMATICA": "OUTROS",
        "STATUS": "PRODUZIDO", "TIPO_PUBLICACAO": "ARQUIVO PDF",
        "LINK_REAL": "SUBPROJETO_7_(FLÁVIO_RAMOS)_CANIE",
        "TAGS": "CADASTRO; CANIE; INFORMAÇÕES; PATRIMÔNIO; ESPELOMETRIA"
    },
    {
        "PROJETO": "TCCE 1/2018", "SUBPROJETO": "SUBPROJETO 12", "AUTOR": "MAURÍCIO CARLOS MARTINS DE ANDRADE",
        "TITULO": "ECOLOGIA DE VERTEBRADOS ASSOCIADOS A CAVERNAS DO ESPINHAÇO MERIDIONAL",
        "DATA": "04/2024", "TIPO_DOCUMENTO": "RELATÓRIO TÉCNICO FINAL", "AREA_TEMATICA": "MEIO BIÓTICO",
        "STATUS": "PRODUZIDO", "TIPO_PUBLICACAO": "ARQUIVO PDF",
        "LINK_REAL": "SUBPROJETO_12_(MAURÍCIO_ANDRADE)_ECOLOGIA_VERTEBRADOS",
        "TAGS": "ECOLOGIA; VERTEBRADO; ESPINHAÇO"
    },
    {
        "PROJETO": "TCCE 1/2018", "SUBPROJETO": "SUBPROJETO 13", "AUTOR": "RODRIGO LOPES FERREIRA",
        "TITULO": "DISPERSÃO VERSUS CONFINAMENTO: ANÁLISE COMPOSICIONAL E DE ESTRUTURA DE HABITAT COMO SUBSÍDIO À COMPREENSÃO DE MECANISMOS RESPONSÁVEIS PELA IDENTIDADE FAUNÍSTICA SUBTERRÂNEA",
        "DATA": "03/2024", "TIPO_DOCUMENTO": "RELATÓRIO TÉCNICO FINAL", "AREA_TEMATICA": "MEIO BIÓTICO",
        "STATUS": "PRODUZIDO", "TIPO_PUBLICACAO": "ARQUIVO PDF",
        "LINK_REAL": "SUBPROJETO_13_(RODRIGO_LOPES)_DISPERSÃO_VERSUS_CONFINAMENTO",
        "TAGS": "DISPERSÃO; CONFINAMENTO; HABITAT; MECANISMO"
    },
    {
        "PROJETO": "TCCE 1/2018", "SUBPROJETO": "SUBPROJETO 16",
        "AUTOR": "FRANCISCO WILLIAN DA CRUZ JÚNIOR, DANIEL DE STEFANO MENIN",
        "TITULO": "EXPOSIÇÃO PERMANENTE NOS CENTROS DE VISITANTES DO PARQUE NACIONAL CAVERNAS DO PERUAÇU",
        "DATA": "12/2024", "TIPO_DOCUMENTO": "RELATÓRIO TÉCNICO FINAL", "AREA_TEMATICA": "OUTROS",
        "STATUS": "PRODUZIDO", "TIPO_PUBLICACAO": "ARQUIVO PDF",
        "LINK_REAL": "SUBPROJETO_16_(CHICO_BILl)_EXPOSIÇÃO_PERUAÇU",
        "TAGS": "EXPOSIÇÃO; VISITANTE; PERUAÇU"
    },
    {
        "PROJETO": "TCCE 1/2018", "SUBPROJETO": "SUBPROJETO 17.1", "AUTOR": "KARINA DIAS DA SILVA",
        "TITULO": "DIVERSIDADE TAXONÔMICA DE INSETOS AQUÁTICOS (EPHEMEROPTERA, PLECOPTERA, TRICHOPTERA, HETEROPTERA, ODONATA ADULTO) NEOTROPICAIS EM IGARAPÉS DAS ÁREAS FERRUGINOSAS DO BRASIL",
        "DATA": "04/2024", "TIPO_DOCUMENTO": "RELATÓRIO TÉCNICO FINAL", "AREA_TEMATICA": "MEIO BIÓTICO",
        "STATUS": "PRODUZIDO", "TIPO_PUBLICACAO": "ARQUIVO PDF",
        "LINK_REAL": "SUBPROJETO_17.1_(KARINA_SILVA)_DIVERSIDADE_TAXONÔMICA",
        "TAGS": "INSETO; AQUÁTICO; NEOTROPICAIS; IGARAPÉS; FERRUGINOSAS; EDITAL"
    },
    {
        "PROJETO": "TCCE 1/2018", "SUBPROJETO": "SUBPROJETO 17.2", "AUTOR": "FABIANA GISELE DA SILVA PINTO",
        "TITULO": "DIVERSIDADE METABARCODING E FUNCIONAL DE COMUNIDADES MICROBIANAS DO SOLO DE CAVERNAS FERRÍFERAS DO PARQUE NACIONAL DOS CAMPOS FERRUGINOSOS - PA",
        "DATA": "04/2024", "TIPO_DOCUMENTO": "RELATÓRIO TÉCNICO FINAL", "AREA_TEMATICA": "OUTROS",
        "STATUS": "PRODUZIDO", "TIPO_PUBLICACAO": "ARQUIVO PDF",
        "LINK_REAL": "SUBPROJETO_17.2_(FABIANA)_DIVERSIDADE_METABARCODING",
        "TAGS": "METABARCODIN; GENÉTICA; MICOLOGIA; FERRUGINOSAS; EDITAL"
    },
    {
        "PROJETO": "TCCE 1/2018", "SUBPROJETO": "SUBPROJETO 17.3", "AUTOR": "ÚRSULA DE AZEVEDO RUCHKYS",
        "TITULO": "ESTUDOS DA PAISAGEM, DA GEODIVERSIDADE E PROPOSTAS DE GEOCONSERVAÇÃO DO GEOSSISTEMA FERRUGINOSO CARAJÁS - PA",
        "DATA": "04/2024", "TIPO_DOCUMENTO": "RELATÓRIO TÉCNICO FINAL", "AREA_TEMATICA": "MEIO FÍSICO",
        "STATUS": "PRODUZIDO", "TIPO_PUBLICACAO": "ARQUIVO PDF",
        "LINK_REAL": "SUBPROJETO_17.3_(ÚRSULA)_ESTUDO_PAISAGEM",
        "TAGS": "GEODIVERSIDADE; GEOCONSERVAÇÃO; FERRUGINOSAS; EDITAL"
    },
    {
        "PROJETO": "TCCE 1/2018", "SUBPROJETO": "SUBPROJETO 17.4",
        "AUTOR": "PAULO EDUARDO DE OLIVEIRA, LUIZA SANTOS REIS",
        "TITULO": "REGISTRO PALEOAMBIENTAIS DE DEPÓSITOS DE GUANO EM CAVERNAS FERRÍFERAS DA FLORESTA NACIONAL DE CARAJÁS",
        "DATA": "04/2024", "TIPO_DOCUMENTO": "RELATÓRIO TÉCNICO FINAL", "AREA_TEMATICA": "OUTROS",
        "STATUS": "PRODUZIDO", "TIPO_PUBLICACAO": "ARQUIVO PDF",
        "LINK_REAL": "SUBPROJETO_17.4_(PAULO_EDUARDO)_REGISTRO_PALEOAMBIENTAIS",
        "TAGS": "PALEOCLIMA; CHIROPTERA; CARAJÁS; FERRUGINOSAS; EDITAL"
    },
    {
        "PROJETO": "TCCE 1/2018", "SUBPROJETO": "SUBPROJETO 17.5", "AUTOR": "THIAGO BERNARDI VIEIRA",
        "TITULO": "PASSADO, PRESENTE E FUTURO PARA A CONSERVAÇÃO DAS ÁREAS CAVERNÍCOLAS E DOS SERVIÇOS ECOSSISTÊMICOS PRESTADOS POR MORCEGOS",
        "DATA": "04/2024", "TIPO_DOCUMENTO": "RELATÓRIO TÉCNICO FINAL", "AREA_TEMATICA": "MEIO BIÓTICO",
        "STATUS": "PRODUZIDO", "TIPO_PUBLICACAO": "ARQUIVO PDF",
        "LINK_REAL": "SUBPROJETO_17.5_(THIAGO_BERNARDI)_PASSADO_PRESENTE_FUTURO",
        "TAGS": "CHIROPTERA; DISTRIBUIÇÃO; ECOSSISTEMA; FERRUGINOSAS; EDITAL"
    },
    {
        "PROJETO": "TCCE 1/2018", "SUBPROJETO": "SUBPROJETO 17.6", "AUTOR": "MICHELINE CARVALHO SILVA",
        "TITULO": "DIVERSIDADE DE ORGANISMOS DO SOLO, EM CAVERNAS EM FORMAÇÃO FERRÍFERA NO QUADRILATERO FERRÍFERO, MINAS GERAIS, BRASIL, COM USO DE DNA METABARCODING",
        "DATA": "01/2025", "TIPO_DOCUMENTO": "RELATÓRIO TÉCNICO FINAL", "AREA_TEMATICA": "MEIO BIÓTICO",
        "STATUS": "PRODUZIDO", "TIPO_PUBLICACAO": "ARQUIVO PDF",
        "LINK_REAL": "SUBPROJETO_17.6_(MICHELINE_SILVA)_DIVERSIDADE_DE_ORGANISMOS",
        "TAGS": "METABARCODIN; GENÉTICA; FERRUGINOSAS; EDITAL"
    },
    {
        "PROJETO": "TCCE 1/2018", "SUBPROJETO": "SUBPROJETO 17.7", "AUTOR": "CRISTINA MARIA DE SOUZA MOTTA",
        "TITULO": "MICOBIOTA DE CAVERNAS DA FLONA CARAJÁS/PA: INVENTÁRIO E SUBSÍDIOS PARA O MANEJO ESPELEOTURÍSTICO",
        "DATA": "04/2024", "TIPO_DOCUMENTO": "RELATÓRIO TÉCNICO FINAL", "AREA_TEMATICA": "MEIO BIÓTICO",
        "STATUS": "PRODUZIDO", "TIPO_PUBLICACAO": "ARQUIVO PDF",
        "LINK_REAL": "SUBPROJETO_17.7_(CRISTINA_MOTTA)_MICOBIOTA_DE_CAVERNAS",
        "TAGS": "INVENTÁRIO; ESPELEOTURISMO; MICOLOGIA; FERRUGINOSAS; EDITAL"
    },
    {
        "PROJETO": "TCCE 1/2018", "SUBPROJETO": "SUBPROJETO 17.8", "AUTOR": "OLINTO LIPARINI PEREIRA",
        "TITULO": "TAXONOMIA E FILOGENIA MOLECULAR DE FUNGOS EM CAVERNAS FERRÍFERAS ENTRE AS REGIÕES DE CONCEIÇÃO DO MATO DENTRO E SERRO, MINAS GERAIS",
        "DATA": "04/2024", "TIPO_DOCUMENTO": "RELATÓRIO TÉCNICO FINAL", "AREA_TEMATICA": "MEIO BIÓTICO",
        "STATUS": "PRODUZIDO", "TIPO_PUBLICACAO": "ARQUIVO PDF",
        "LINK_REAL": "SUBPROJETO_17.8_(OLINTO_LIPARINI)_TAXONOMIA_E_FILOGENIA",
        "TAGS": "TAXONÔMIA; GENÉTICA; MICOLOGIA; FERRUGINOSAS; EDITAL"
    },
    {
        "PROJETO": "TCCE 2/2020", "SUBPROJETO": "SUBPROJETO 1",
        "AUTOR": "RICARDO GALENO FRAGA DE ARAÚJO PEREIRA, TARSILA CARVALHO DE JESUS",
        "TITULO": "CARACTERIZAÇÃO E REGIONALIZAÇÃO DOS TERRENOS CÁRSTICOS, EM ROCHAS CARBONÁTICAS, NO ESTADO DA BAHIA",
        "DATA": "04/2023", "TIPO_DOCUMENTO": "RELATÓRIO TÉCNICO FINAL", "AREA_TEMATICA": "MEIO FÍSICO",
        "STATUS": "PRODUZIDO", "TIPO_PUBLICACAO": "ARQUIVO PDF",
        "LINK_REAL": "SUBPROJETO_1_(RICARDO_FRAGA)_CARACTERIZAÇÃO",
        "TAGS": "CARACTERIZAÇÃO; CARSTE; CARBONÁTICA;"
    },
    {
        "PROJETO": "TCCE 2/2020", "SUBPROJETO": "SUBPROJETO 3", "AUTOR": "MARIA ELINA BICHUETTE",
        "TITULO": "TESTE DE METODOLOGIAS PROPOSTAS EM LEGISLAÇÃO AMBIENTAL RELACONADAS À FAUNA SUBTERRÂNEA E PROPOSIÇÃO DE NOVAS ÁREAS PRIORITÁRIAS PARA CONSERVAÇÃO DE CAVERNAS",
        "DATA": "04/2025", "TIPO_DOCUMENTO": "RELATÓRIO TÉCNICO FINAL", "AREA_TEMATICA": "OUTROS",
        "STATUS": "PRODUZIDO", "TIPO_PUBLICACAO": "ARQUIVO PDF",
        "LINK_REAL": "SUBPROJETO_3_(MARIA_ELINA)_TESTE_DE_METODOLOGIA",
        "TAGS": "CONSERVAÇÃO; PRIORITÁRIA; PATRIMÔNIO; LEGISLAÇÃO"
    },
    {
        "PROJETO": "TCCE 2/2020", "SUBPROJETO": "SUBPROJETO 5",
        "AUTOR": "LUCIANA DE RESENDE ALT, VITOR MARCOS AGUIAR DE MOURA",
        "TITULO": "INTRODUÇÃO ÀS PRÁTICAS DE CONSERVAÇÃO E RECUPERAÇÃO AMBIENTAL EM CAVERNAS TURÍSTICAS",
        "DATA": "12/2023", "TIPO_DOCUMENTO": "RELATÓRIO TÉCNICO FINAL", "AREA_TEMATICA": "OUTROS",
        "STATUS": "PRODUZIDO", "TIPO_PUBLICACAO": "ARQUIVO PDF",
        "LINK_REAL": "SUBPROJETO_5_(LUCIANA_ALT)_RECUPERAÇÃO_AMBIENTAL",
        "TAGS": "CONSERVAÇÃO; RECUPERAÇÃO; ESPELEOTURISMO; IMPACTO"
    },
    {
        "PROJETO": "TCCE 2/2020", "SUBPROJETO": "SUBPROJETO 8", "AUTOR": "JOÃO MARCELO TEIXEIRA",
        "TITULO": "MODELAGEM 3D DE CAVIDADES NATURAIS SUBTERRÂNEAS",
        "DATA": "07/2023", "TIPO_DOCUMENTO": "RELATÓRIO TÉCNICO FINAL", "AREA_TEMATICA": "OUTROS",
        "STATUS": "PRODUZIDO", "TIPO_PUBLICACAO": "ARQUIVO PDF",
        "LINK_REAL": "SUBPROJETO_8_(JOÃO_MARCELO)_MODELAGEM_3D",
        "TAGS": "SOFTWARE; MODELAGEM; RECONSTRUÇÃO; IPHONE"
    },
    {
        "PROJETO": "TCCE 2/2020", "SUBPROJETO": "SUBPROJETO 10", "AUTOR": "ENRICO BERNARD",
        "TITULO": "AMPLIAÇÃO DA PESQUISA E CONSERVAÇÃO DE MORCEGOS BRASILEIROS: UMA PROPOSTA DA SBEQ",
        "DATA": "05/2024", "TIPO_DOCUMENTO": "RELATÓRIO TÉCNICO FINAL", "AREA_TEMATICA": "MEIO BIÓTICO",
        "STATUS": "PRODUZIDO", "TIPO_PUBLICACAO": "ARQUIVO PDF",
        "LINK_REAL": "SUBPROJETO_10_(ENRICO)_AMPLIAÇÃO_PESQUISA_MORCEGOS",
        "TAGS": "CHIROPTERA; CONSERVAÇÃO; SBEQ; EDITAL"
    },
    {
        "PROJETO": "TCCE 2/2020", "SUBPROJETO": "SUBPROJETO 13", "AUTOR": "ALLAN SILAS CALUX",
        "TITULO": "PRÓ-CAVERNAS",
        "DATA": "04/2025", "TIPO_DOCUMENTO": "RELATÓRIO TÉCNICO FINAL", "AREA_TEMATICA": "OUTROS",
        "STATUS": "PRODUZIDO", "TIPO_PUBLICACAO": "ARQUIVO PDF",
        "LINK_REAL": "SUBPROJETO_13_(ALLAN_CALUX)_PRÓ_CAVERNAS",
        "TAGS": "SBE; CNC; ACERVO; EDTAL"
    },
    {
        "PROJETO": "TCCE 2/2020", "SUBPROJETO": "SUBPROJETO 13.1", "AUTOR": "MAURO DE OLIVEIRA NETO",
        "TITULO": "PROSPECÇÃO E MAPEAMENTO DE CAVERNAS NA SERRA DO ITAQUERI - SÃO PAULO",
        "DATA": "10/2024", "TIPO_DOCUMENTO": "RELATÓRIO TÉCNICO FINAL", "AREA_TEMATICA": "OUTROS",
        "STATUS": "PRODUZIDO", "TIPO_PUBLICACAO": "ARQUIVO PDF",
        "LINK_REAL": "AJUSTAR DOCUMENTO",
        "TAGS": "PROSPECÇÃO; EXPLORAÇÃO; TOPOGRAFIA; MAPEAMENTO; EDITAL"
    },
    {
        "PROJETO": "TCCE 2/2020", "SUBPROJETO": "SUBPROJETO 13.2", "AUTOR": "PAULO HENRIQUE ROSADO ARENAS",
        "TITULO": "VALE DO RIO GAMELEIRA - REDESCOBERTAS ESPELEOLÓGICAS NO P. A. GAMELEIRA E ENTORNO - FLORWS DE GOIÁS/GO",
        "DATA": "10/2024", "TIPO_DOCUMENTO": "RELATÓRIO TÉCNICO FINAL", "AREA_TEMATICA": "OUTROS",
        "STATUS": "PRODUZIDO", "TIPO_PUBLICACAO": "ARQUIVO PDF",
        "LINK_REAL": "SUBPROJETO_13.2_(PAULO_ARENAS)_AMPLIANDO_ROTAS_1",
        "TAGS": "PROSPECÇÃO; EXPLORAÇÃO; TOPOGRAFIA; MAPEAMENTO; EDITAL"
    },
    {
        "PROJETO": "TCCE 2/2020", "SUBPROJETO": "SUBPROJETO 13.3", "AUTOR": "NEI ALVES GONDIM JÚNIOR",
        "TITULO": "TOPOGRAFIA DAS GRUTAS BARRIGUDAS, URUBUS, SALITRE E XIRANHA NO MORRO DAS ARARAS, MUNICÍPIO DE ITUAÇI, BAHIA - BRASIL",
        "DATA": "10/2024", "TIPO_DOCUMENTO": "RELATÓRIO TÉCNICO FINAL", "AREA_TEMATICA": "OUTROS",
        "STATUS": "PRODUZIDO", "TIPO_PUBLICACAO": "ARQUIVO PDF",
        "LINK_REAL": "SUBPROJETO_13.3_(NEI_ALVES)_AMPLIANDO_ROTAS_1",
        "TAGS": "PROSPECÇÃO; EXPLORAÇÃO; TOPOGRAFIA; MAPEAMENTO; EDITAL"
    },
    {
        "PROJETO": "TCCE 2/2020", "SUBPROJETO": "SUBPROJETO 13.4", "AUTOR": "EDENILSON ROBERTO DO NASCIMENTO",
        "TITULO": "ATUALIZAÇÃO E ADEQUAÇÃO DO CADASTRO DAS INFORMAÇÕES ESPELEOLÓGICAS DO MUNICÍPIO DE RIO BRANCO DO SUL - PR",
        "DATA": "10/2024", "TIPO_DOCUMENTO": "RELATÓRIO TÉCNICO FINAL", "AREA_TEMATICA": "OUTROS",
        "STATUS": "PRODUZIDO", "TIPO_PUBLICACAO": "ARQUIVO PDF",
        "LINK_REAL": "SUBPROJETO_13.4_(EDENILSON)_AMPLIANDO_ROTAS_1",
        "TAGS": "PROSPECÇÃO; EXPLORAÇÃO; TOPOGRAFIA; MAPEAMENTO; EDITAL"
    },
    {
        "PROJETO": "TCCE 2/2020", "SUBPROJETO": "SUBPROJETO 13.5", "AUTOR": "CARLOS FREDERICO DE SOUZA LOTT",
        "TITULO": "PROSPECÇÃO E TOPOGRAFIA DE CAVERNAS NA PORÇÃO NORTE DA SERRA DO BALDIM",
        "DATA": "10/2024", "TIPO_DOCUMENTO": "RELATÓRIO TÉCNICO FINAL", "AREA_TEMATICA": "OUTROS",
        "STATUS": "PRODUZIDO", "TIPO_PUBLICACAO": "ARQUIVO PDF",
        "LINK_REAL": "SUBPROJETO_13.5_(FRED_LOTT)_AMPLIANDO_ROTAS_1",
        "TAGS": "PROSPECÇÃO; EXPLORAÇÃO; TOPOGRAFIA; MAPEAMENTO; EDITAL"
    },
    {
        "PROJETO": "TCCE 2/2020", "SUBPROJETO": "SUBPROJETO 13.6", "AUTOR": "LUCIANO EMERICH FARIA",
        "TITULO": "O GRANDE ROTEIRO DE PETER LUND - PARTE II: AS CAVERNAS NÃO VISITADAS POR LUND, PORÉM REVELADAS PELO PROJETO",
        "DATA": "10/2024", "TIPO_DOCUMENTO": "RELATÓRIO TÉCNICO FINAL", "AREA_TEMATICA": "OUTROS",
        "STATUS": "PRODUZIDO", "TIPO_PUBLICACAO": "ARQUIVO PDF",
        "LINK_REAL": "SUBPROJETO_13.6_(FÁBIO_KHALED)_AMPLIANDO_ROTAS_1",
        "TAGS": "PROSPECÇÃO; EXPLORAÇÃO; TOPOGRAFIA; MAPEAMENTO; EDITAL"
    },
    {
        "PROJETO": "TCCE 2/2020", "SUBPROJETO": "SUBPROJETO 13.7", "AUTOR": "FÁBIO AZEVEDO KHALED ABDEL RAHMAN",
        "TITULO": "CAVERNAS DA SERRA NEGRA - PROSPECÇÃO, EXPLORAÇÃO, TOPOGRAFIA, MAPEAMENTO E LEVANTAMENTO FAUNÍSTICO E AVALIAÇÃO ARQUEOLÓGICA DAS CAVIDADES NATURAIS DO PARQUE ESTADUAL DE SERRA NEGRA DA MANTIQUEIRA, MG, E ÁREAS DO ENTORNO",
        "DATA": "10/2024", "TIPO_DOCUMENTO": "RELATÓRIO TÉCNICO FINAL", "AREA_TEMATICA": "OUTROS",
        "STATUS": "PRODUZIDO", "TIPO_PUBLICACAO": "ARQUIVO PDF",
        "LINK_REAL": "SUBPROJETO_13.7_(LUCIANO_FARIAS)_AMPLIANDO_ROTAS_1",
        "TAGS": "PROSPECÇÃO; EXPLORAÇÃO; TOPOGRAFIA; MAPEAMENTO; EDITAL"
    },
    {
        "PROJETO": "TCCE 1/2022", "SUBPROJETO": "SUBPROJETO 1", "AUTOR": "GISELE CRISTINA SESSEGOLO",
        "TITULO": "37º CONGRESSO BRASILEIRO DE ESPELEOLOGIA",
        "DATA": "10/2023", "TIPO_DOCUMENTO": "RELATÓRIO TÉCNICO FINAL", "AREA_TEMATICA": "OUTROS",
        "STATUS": "PRODUZIDO", "TIPO_PUBLICACAO": "ARQUIVO PDF",
        "LINK_REAL": "SUBPROJETO_1_(GISELE_SESSEGOLO)_37_CBE",
        "TAGS": "CONGRESSO, ESPELEOLOGIA; BRASIL"
    },
    {
        "PROJETO": "TCCE 1/2022", "SUBPROJETO": "SUBPROJETO 5", "AUTOR": "LEONARDO TORTORIELLO MESSIAS",
        "TITULO": "RECIFE DE CORAL - AS CAVERNAS SUBMARINAS DO NORDESTE DO BRASIL",
        "DATA": "10/2025", "TIPO_DOCUMENTO": "RELATÓRIO TÉCNICO FINAL", "AREA_TEMATICA": "OUTROS",
        "STATUS": "PRODUZIDO", "TIPO_PUBLICACAO": "ARQUIVO PDF",
        "LINK_REAL": "SUBPROJETO_5_(LEONARDO_MESSIAS)_RECIFES_DE_CORAL",
        "TAGS": "CORAL; SUBMARINAS; SUBAQUÁTICAS; REEF"
    },
    {
        "PROJETO": "TCCE 1/2022", "SUBPROJETO": "SUBPROJETO 6", "AUTOR": "IVAN BRAGA CAMPOS",
        "TITULO": "PAISAGEM SONORA DE CAVERNAS E DOS ECOSSISTEMAS EM SEU ENTORNO DO PARQUE NACIONAL DA SERRA DO CIPÓ",
        "DATA": "10/2025", "TIPO_DOCUMENTO": "RELATÓRIO TÉCNICO FINAL", "AREA_TEMATICA": "OUTROS",
        "STATUS": "PRODUZIDO", "TIPO_PUBLICACAO": "ARQUIVO PDF",
        "LINK_REAL": "SUBPROJETO_6_(IVAN_BRAGA)_RECIFES_DE_CORAL",
        "TAGS": "PAISAGEM; BIOACÚSTICA; GRAVAÇÃO;"
    },
    {
        "PROJETO": "TCCE 1/2022", "SUBPROJETO": "SUBPROJETO 9", "AUTOR": "LEDA ZOGBI",
        "TITULO": "LUZES NA ESCURIDÃO - VOLUME 3",
        "DATA": "06/2024", "TIPO_DOCUMENTO": "RELATÓRIO TÉCNICO FINAL", "AREA_TEMATICA": "OUTROS",
        "STATUS": "PRODUZIDO", "TIPO_PUBLICACAO": "ARQUIVO PDF",
        "LINK_REAL": "SUBPROJETO_9_(LEDA_ZOGBI)_LUZES",
        "TAGS": "ESPELEOFOTOGRAFIA; FOTOGRAFIA; LUZES; ESCURIDÃO"
    },
    {
        "PROJETO": "TCCE 1/2022", "SUBPROJETO": "SUBPROJETO 10",
        "AUTOR": "PAULO HENRIQUE FERREIRA GALVÃO, LUCAS PADOAN DE SÁ GODINHO",
        "TITULO": "APLICAÇÃO DE TRAÇADORES CORANTES PARA CARACTERIZAÇÃO DA DINÂMICA ATUAL DE FLUXO D'ÁGUA SUBTERRÂNEA NO CARSTE DE SÃO DESIDÉRIO, BAHIA, BRASIL",
        "DATA": "08/2025", "TIPO_DOCUMENTO": "RELATÓRIO TÉCNICO FINAL", "AREA_TEMATICA": "OUTROS",
        "STATUS": "PRODUZIDO", "TIPO_PUBLICACAO": "ARQUIVO PDF",
        "LINK_REAL": "SUBPROJETO_10_(PAULO_GALVÃO)_TRAÇADORES",
        "TAGS": "TRAÇADORES; HIDROLOGIA; CARSTE; FLUXO"
    },
    {
        "PROJETO": "TCCE 1/2022", "SUBPROJETO": "SUBPROJETO 20", "AUTOR": "ZACARIAS TARGINO DE FREITAS NETO",
        "TITULO": "SERVIÇO DE REFORMA ESTRUTURA FÍSICA DO MUSEU ARQUEOLÓGICO DO LAJEDO DE SOLEDADE",
        "DATA": "05/2024", "TIPO_DOCUMENTO": "RELATÓRIO TÉCNICO FINAL", "AREA_TEMATICA": "OUTROS",
        "STATUS": "PRODUZIDO", "TIPO_PUBLICACAO": "ARQUIVO PDF",
        "LINK_REAL": "SUBPROJETO_20_(ZACARIAS)_REFORMA_LAJEDO",
        "TAGS": "REFORMA; MUSEU; LAJEDO; HISTÓRIA"
    },
    {
        "PROJETO": "TCCE 1/2022", "SUBPROJETO": "SUBPROJETO 18.10", "AUTOR": "ANTÔNIO CALAZANS REIS MIRANDA",
        "TITULO": "PATRIMÔNIO ESPELEOLÓGICO DA APA CARSTE DE LAGOA SANTA: CONHECER PARA CONSERVAR E PROTEGER PELA EDUCOMUNICAÇÃO",
        "DATA": "09/2024", "TIPO_DOCUMENTO": "RELATÓRIO TÉCNICO FINAL", "AREA_TEMATICA": "OUTROS",
        "STATUS": "PRODUZIDO", "TIPO_PUBLICACAO": "ARQUIVO PDF",
        "LINK_REAL": "SUBPROJETO_18.10_(ANTÔNIO_CALAZANS)_EDUCOMUNICAÇÃO",
        "TAGS": "EDUCOMUNICAÇÃO; ESPELEOTURISMO; GRÁFICO"
    },
    {
        "PROJETO": "TCCE 1/2022", "SUBPROJETO": "SUBPROJETO 22 (AÇÃO 4.20.1)",
        "AUTOR": "REGIANNE KELLY MOREIRA DA SILVA",
        "TITULO": "MULTIVERSO ESPELEOLÓGICO",
        "DATA": "06/2024", "TIPO_DOCUMENTO": "RELATÓRIO TÉCNICO FINAL", "AREA_TEMATICA": "OUTROS",
        "STATUS": "PRODUZIDO", "TIPO_PUBLICACAO": "ARQUIVO PDF",
        "LINK_REAL": "SUBPROJETO_22_AÇÃO_4.20.1_(REGIANNE)_MULTIVERSO_ESPELEOLOGICO",
        "TAGS": "ENDURO; ESPELEOLOGIA; BRASIL"
    },
    {
        "PROJETO": "TCCE 1/2022", "SUBPROJETO": "SUBPROJETO 22 (AÇÃO 4.20.2)",
        "AUTOR": "DAYANNE FERREIRA DOS SANTOS SIRQUEIRA",
        "TITULO": "CONSULTA LIVRE PRÉVIA E INFORMADA",
        "DATA": "03/2025", "TIPO_DOCUMENTO": "RELATÓRIO TÉCNICO FINAL", "AREA_TEMATICA": "OUTROS",
        "STATUS": "PRODUZIDO", "TIPO_PUBLICACAO": "ARQUIVO PDF",
        "LINK_REAL": "SUBPROJETO_22_AÇÃO_4.20.2_(DAYANNE)_PERUAÇU",
        "TAGS": "CLPI; REUNIÃO; TRADICIONAIS; INDÍGENA; PERUAÇU"
    },
    {
        "PROJETO": "TCCE 1/2022", "SUBPROJETO": "SUBPROJETO 22 (AÇÃO 4.20.3)",
        "AUTOR": "DAYANNE FERREIRA DOS SANTOS SIRQUEIRA",
        "TITULO": "III SEMINÁRIO CIENTÍFICO DO VALE DO PERUAÇU - SCIVAPE",
        "DATA": "03/2025", "TIPO_DOCUMENTO": "RELATÓRIO TÉCNICO FINAL", "AREA_TEMATICA": "OUTROS",
        "STATUS": "PRODUZIDO", "TIPO_PUBLICACAO": "ARQUIVO PDF",
        "LINK_REAL": "SUBPROJETO_22_AÇÃO_4.20.3_(DAYANNE)_PERUAÇU",
        "TAGS": "SEMINÁRIO; TÉCNICO; PESQUISA; COMUNIDADE; PERUAÇU"
    }
]


# --------------------------------------------------------------------------------
# 4. FUNÇÃO PRINCIPAL DE IMPORTAÇÃO
# --------------------------------------------------------------------------------

def run_import():
    registros_criados_count = 0
    erros = []

    # 1. Obter o usuário padrão (Assumindo que o superusuário 1 é o usuário de auditoria)
    try:
        # Busca o primeiro superusuário ativo ou o primeiro usuário ativo.
        auditor_user = User.objects.filter(is_superuser=True, is_active=True).first()
        if not auditor_user:
            auditor_user = User.objects.filter(is_active=True).first()
        if not auditor_user:
            raise ObjectDoesNotExist("Nenhum usuário ativo encontrado para auditoria. Crie um superusuário primeiro.")
    except ObjectDoesNotExist as e:
        print(f"ERRO CRÍTICO: {e}")
        return

    print(f"Usuário de Auditoria: {auditor_user.email}")
    print(f"Total de itens a importar: {len(ITENS)}")

    with transaction.atomic():
        for i, item_data in enumerate(ITENS):
            try:
                # --- A. Busca de Chaves Estrangeiras (FKs) ---

                # 1. Subprojeto (Depende do Projeto e Subprojeto nome)
                projeto = Projeto.objects.get(nome=item_data["PROJETO"])
                subprojeto = Subprojeto.objects.get(
                    projeto=projeto,
                    nome=item_data["SUBPROJETO"]
                )

                # 2. Tipos e Áreas (Busca simples por nome)
                tipo_documento = TipoDocumento.objects.get(nome=item_data["TIPO_DOCUMENTO"])
                area_tematica = AreaTematica.objects.get(nome=item_data["AREA_TEMATICA"])
                status = Status.objects.get(nome=item_data["STATUS"])
                tipo_publicacao = TipoPublicacao.objects.get(nome=item_data["TIPO_PUBLICACAO"])

                # 3. Data de Publicação (Converte string MM/YYYY para Python date)
                data_publicacao_str = item_data["DATA"]
                data_publicacao = None
                if '/' in data_publicacao_str:
                    try:
                        # Tenta MM/YYYY, usando o dia 01
                        data_publicacao = datetime.strptime(f'01/{data_publicacao_str}', '%d/%m/%Y').date()
                    except ValueError:
                        print(f"AVISO: Formato de data inválido para {item_data['TITULO']}. Usando data nula.")

                # --- B. Criação do Registro Principal ---

                registro = Registro.objects.create(
                    subprojeto=subprojeto,
                    tipo_documento=tipo_documento,
                    area_tematica=area_tematica,
                    status=status,
                    tipo_publicacao=tipo_publicacao,

                    titulo=item_data["TITULO"],
                    data_publicacao=data_publicacao,

                    # LINK_REAL (usado como nome de arquivo simulado)
                    arquivo=f'{item_data["LINK_REAL"]}.pdf',

                    # Auditoria
                    usuario_criacao=auditor_user,
                    usuario_ultima_atualizacao=auditor_user,
                    ativo=True
                )

                # --- C. Relações Many-to-Many (M2M): Autores e Tags ---

                # 4. Autores
                # Split no formato "Autor A, Autor B, Autor C"
                autores_list = [a.strip() for a in item_data["AUTOR"].split(',') if a.strip()]
                for autor_nome in autores_list:
                    try:
                        autor = Autor.objects.get(nome=autor_nome)
                        registro.autores.add(autor)
                    except Autor.DoesNotExist:
                        print(
                            f"AVISO: Autor '{autor_nome}' não encontrado e será ignorado para o registro '{registro.titulo}'")

                # 5. Tags
                # Split no formato "TAG1; TAG2; TAG3"
                tags_list = [t.strip() for t in item_data["TAGS"].split(';') if t.strip()]
                for tag_nome in tags_list:
                    # Remove caracteres como ',' e '. ' acidentalmente inclusos no split
                    tag_nome_limpo = tag_nome.replace(',', '').replace('.', '').strip()
                    try:
                        tag = Tag.objects.get(nome=tag_nome_limpo)
                        registro.tags.add(tag)
                    except Tag.DoesNotExist:
                        # Este caso não deve ocorrer se o SQL de carga inicial foi rodado corretamente
                        print(
                            f"AVISO: Tag '{tag_nome_limpo}' não encontrada e será ignorada para o registro '{registro.titulo}'")

                registros_criados_count += 1
                print(f"SUCESSO ({i + 1}/{len(ITENS)}): Registro criado: {registro.titulo[:50]}...")

            except ObjectDoesNotExist as e:
                erros.append(
                    f"ERRO DE DADOS ({i + 1}/{len(ITENS)}): Chave FK não encontrada - {e}. Item: {item_data['TITULO']}")
                # Re-lança a exceção para forçar o rollback se for um erro de FK
                raise
            except Exception as e:
                erros.append(f"ERRO INESPERADO ({i + 1}/{len(ITENS)}): {e}. Item: {item_data['TITULO']}")
                # Re-lança a exceção para forçar o rollback
                raise

    if erros:
        print("\n--- ERROS ENCONTRADOS ---")
        for erro in erros:
            print(erro)
        print("Transação revertida devido a erros.")
    else:
        print("\n--- RESULTADO FINAL ---")
        print(f"Importação de {registros_criados_count} Registros concluída com sucesso!")


if __name__ == "__main__":
    print("Iniciando importação de Registros...")
    run_import()
    print("Importação finalizada.")