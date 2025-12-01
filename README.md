Repositório TCCEs - Acervo Digital Institucional

📚 Visão Geral do Projeto

O Repositório TCCEs é um sistema web robusto desenvolvido em Python (Django) para a criação, indexação, armazenamento e disponibilização de um acervo digital de documentos e publicações. O objetivo é criar um repositório institucional escalável, com foco em metadados ricos, pesquisa avançada e fluxo de trabalho de catalogação.

Principais Objetivos

- Acervo Digital: Armazenamento e versionamento de arquivos (PDFs, EPUBs, Imagens, etc.).
- Metadados Ricos: Indexação detalhada de metadados (Autor, Data, DOI, ISBN, Palavras-chave, Coleção/Projeto).
- Acesso Público: Páginas públicas de navegação e pesquisa sem necessidade de autenticação.
- Gerenciamento Administrativo: Interface administrativa para cadastro, edição, revisão e gerenciamento de usuários.
- Pesquisa Avançada: Suporte a pesquisa full-text e filtros facetados (por Autor, Ano, Coleção, etc.).

🏗️ Arquitetura e Tecnologias

O projeto segue uma arquitetura modular baseada em Django e é otimizado para escalabilidade e deploy em nuvem.

Camada

Tecnologia

Propósito

Backend

Django (View Functions)

Framework Web principal, lógica de negócio.

Frontend

Django Templates, Bootstrap 5

Interface responsiva e design web.

Banco de Dados

PostgreSQL

Armazenamento relacional robusto e busca full-text (tsvector/pg_trgm).

Armazenamento

AWS S3 (via django-storages)

Armazenamento de objetos (arquivos de documentos) em produção.

Configuração

django-environ

Gerenciamento seguro de variáveis de ambiente (.env).

📁 Estrutura de Diretórios

O projeto é dividido em um diretório principal (repositoriotcce/) e um subdiretório backend/ para o código-fonte Django.

repositoriotcce/

├── .env.example              # Modelo para variáveis de ambiente (NÃO deve ser versionado)

├── requirements.txt          # Dependências do projeto

├── backend/                  # Diretório principal do Django

│   ├── manage.py             # Script de gerenciamento do Django

│   ├── .gitignore            # Regras de ignorar arquivos no escopo do backend

│   ├── config/               # Configurações globais (settings, urls, wsgi)

│   ├── apps/                 # Diretório para Apps modulares do Django

│   │   ├── core/             # Páginas de navegação geral (Home, Sobre, Contato)

│   │   ├── accounts/         # Modelo User Customizado (login por email) e autenticação

│   │   ├── repositorio/      # Modelos de Dados e Lógica do Acervo (Documento, Autor, etc.)

│   │   ├── search/           # Lógica de busca e indexação

│   │   └── (outros apps...)

│   ├── templates/            # Templates globais e modularização (base.html, includes)

│   └── frontend/             # Assets estáticos (CSS, JS, Imagens, Logos)

│       └── static/


🚀 Configuração Local (Passo a Passo)

Siga os passos abaixo para configurar e rodar o projeto em seu ambiente de desenvolvimento.

Pré-requisitos

Você deve ter instalados:

Python (3.x)

Git

PostgreSQL (Servidor rodando localmente, ex: porta 5432)

1. Clonar e Configurar o Ambiente

# 1. Clone o repositório
git clone [https://github.com/](https://github.com/)<SEU_USUARIO>/repositoriotcce-django.git
cd repositoriotcce-django

# 2. Crie e ative um ambiente virtual
python -m venv .venv
source .venv/bin/activate  # ou .venv\Scripts\activate no Windows

# 3. Instale as dependências
pip install -r requirements.txt


2. Configuração de Variáveis de Ambiente

O projeto usa django-environ para carregar configurações sensíveis a partir de um arquivo .env.

Crie uma cópia do arquivo de modelo na raiz do projeto:

cp .env.example .env


Edite o arquivo .env (que está no seu .gitignore) e defina as variáveis:

# Exemplo de conteúdo do .env
DEBUG=True
SECRET_KEY=sua-chave-secreta-longa-e-complexa-aqui-XXXX

# Configuração do seu PostgreSQL local
DATABASE_URL=postgres://postgres:minhasenha@localhost:5432/my_archive_db

# Se não for usar S3 localmente, pode deixar as chaves AWS vazias por enquanto.
AWS_ACCESS_KEY_ID=
AWS_SECRET_ACCESS_KEY=
AWS_STORAGE_BUCKET_NAME=


3. Configuração do Banco de Dados e Usuário

Certifique-se de que seu servidor PostgreSQL esteja ativo e o banco de dados especificado em DATABASE_URL exista.

cd backend

# 1. Crie as migrações iniciais (User Customizado e Modelos do Repositorio)
python manage.py makemigrations accounts
python manage.py makemigrations repositorio

# 2. Aplique todas as migrações ao banco de dados
python manage.py migrate

# 3. Crie um Superusuário (login será via email)
python manage.py createsuperuser


4. Executar o Servidor

# 4. Inicie o servidor de desenvolvimento
python manage.py runserver

# Acesse:
# Site: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
# Admin: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)


🛠️ Boas Práticas e Fluxo de Trabalho

Custom User Model: O login é feito utilizando o campo email em vez do username.

Static/Media Files: Em desenvolvimento (DEBUG=True), arquivos de mídia são servidos localmente. Em produção, eles são automaticamente roteados para o AWS S3 (configurado via settings.py).

I18n: Uso de gettext_lazy (_) em Models e Apps para internacionalização/tradução futura.

👥 Perfis de Usuário Implementados

Administrador / Catalogador: Acesso total à interface administrativa para CRUD de documentos, metadados e gerenciamento de usuários.

Usuário Final / Leitor: Acesso público ao repositório para pesquisa e visualização de documentos publicados.