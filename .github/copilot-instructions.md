# Instrucoes do projeto

Estas instrucoes se aplicam a este repositorio Django.

## Estrutura real

- `manage.py` fica na raiz do repositorio.
- Os aplicativos Django ficam em `apps/`: `core`, `accounts` e `repositorio`.
- A configuracao do projeto Django fica em `repositoriotcce/`.
- Templates e arquivos estaticos ficam em `www/templates/` e `www/static/`.
- Arquivos de midia ficam em `www/media/`.
- Os testes do repositorio ficam em `apps/repositorio/tests/`.

A documentacao existente pode mencionar uma estrutura `backend/`; use a estrutura real do workspace como fonte de verdade para edicoes e comandos.

## Ambiente e comandos

- Este projeto nao utiliza Docker por enquanto. Nao introduza Docker nem use `docker compose` para executar comandos.
- Use o interpretador Python e o ambiente virtual ja configurados no workspace, quando existirem. Nao crie um novo ambiente virtual sem necessidade.
- Execute comandos Django a partir da raiz, por exemplo: `python manage.py check` e `python manage.py test`.
- Antes de instalar dependencias ou alterar o ambiente, verifique `requirements.txt` e a configuracao atual do workspace.
- Nao exponha valores de `.env` em respostas, logs, diffs ou arquivos versionados.

## Como trabalhar

- Antes de editar, localize a implementacao que realmente decide o comportamento e consulte usos, testes e configuracoes proximos.
- Formule uma hipotese curta sobre a causa ou o comportamento esperado e escolha uma verificacao que possa confirma-la ou refuta-la.
- Prefira a menor mudanca compativel com os padroes existentes do projeto. Evite refatoracoes ou formatacoes sem relacao com a tarefa.
- Preserve APIs publicas, nomes, convencoes Django e comportamento existente, salvo quando a tarefa exigir mudanca.
- Ao alterar modelos, avalie explicitamente se uma migration e necessaria. Nao edite migrations antigas para corrigir um estado ja aplicado; crie uma nova migration quando apropriado.
- Nao altere dados, cargas iniciais, banco, arquivos de media ou configuracoes de producao sem necessidade clara. Para operacoes destrutivas ou de alto impacto, solicite confirmacao antes de executa-las.
- Nao modifique mudancas existentes do usuario nem reverta arquivos que nao fazem parte da tarefa.

## Validacao

- Depois de uma edicao, execute primeiro a verificacao mais focada disponivel para o comportamento alterado.
- Para mudancas Django, priorize testes especificos do app ou caso afetado e depois `python manage.py check` quando aplicavel.
- Use a configuracao de testes existente antes de concluir qual banco ou ambiente esta sendo usado. `repositoriotcce/settings_test.py` configura SQLite para testes, mas o settings efetivo deve ser confirmado pelo comando executado.
- Se uma validacao nao puder ser executada por falta de dependencia, servico ou configuracao, informe o bloqueio e nao apresente a tarefa como totalmente validada.

## Seguranca

- Nunca leia, copie ou revele segredos de `.env`, chaves AWS, senhas, tokens ou credenciais.
- Evite incluir dados pessoais, registros reais ou conteudo sensivel em exemplos, logs e testes.
- Nao versionar banco local, arquivos gerados, credenciais ou arquivos de media ignorados pelo repositorio.
- Ao trabalhar com upload, download, autenticacao, autorizacao ou arquivos, considere validacao de entrada, controle de acesso e exposicao acidental de dados.

## Comunicacao

- Responda em portugues do Brasil.
- Seja conciso e indique a decisao tecnica, os arquivos alterados, os comandos executados e o resultado das validacoes.
- Ao encontrar documentacao desatualizada, diferencie o que foi observado no workspace do que esta documentado; nao altere a documentacao sem que isso faca parte da tarefa.
