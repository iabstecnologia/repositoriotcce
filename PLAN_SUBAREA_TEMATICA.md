# Plano: CRUD de Subárea Temática e filtro na Busca Avançada

## Contexto identificado

- O app `repositorio` já possui o CRUD de `AreaTematica`, com views base reutilizáveis, formulário genérico de metadados, rotas protegidas por login e menu de Gestão.
- `Registro` hoje possui uma FK obrigatória para `AreaTematica`; a busca pública aplica o filtro em `apps/core/repository_filters.py` e renderiza os campos em `repository_advanced_filters.html`.
- A área temática ainda não possui relação com subáreas, e o cadastro/edição de `Registro` não oferece esse campo.

## Decisão de modelagem recomendada

Criar `SubAreaTematica` como entidade de metadado:

- `area_tematica`: FK para `AreaTematica`, `on_delete=PROTECT`, permitindo uma área com uma ou várias subáreas.
- `nome`: nome da subárea, normalizado pelo formulário e único dentro da área (`UniqueConstraint` em `area_tematica` + `nome`).
- As categorias `Meio Físico`, `Meio Biótico` e `Outros` são registros existentes de `AreaTematica`; não haverá campo duplicado `meio` em `SubAreaTematica`.
- `ativo`: controle de disponibilidade, seguindo os demais metadados.

Adicionar em `Registro` uma relação ManyToMany `subareas_tematicas` para `SubAreaTematica`. A relação ficará opcional no banco para preservar registros existentes, mas será obrigatória no formulário de novos registros. Registros legados poderão permanecer sem subárea até eventual saneamento.

## Escopo de implementação

### 1. Banco e domínio

1. Adicionar `SubAreaTematica` em `apps/repositorio/models/repositorio.py`, exportá-la em `apps/repositorio/models/__init__.py` e registrá-la no admin.
2. Adicionar a relação ManyToMany `subareas_tematicas` em `Registro`, com verbose names e `prefetch_related` nos fluxos que carregam registros.
3. Criar migração do schema.
4. Criar migração de dados/seed idempotente para as nove opções iniciais:
   - **Meio Físico:** Geologia e Geomorfologia; Hidrologia e Hidrogeologia; Espeleologia e Caracterização Ambiental.
   - **Meio Biótico:** Biodiversidade Subterrânea; Ecologia; Conservação da biodiversidade.
   - **Outros:** Socioeconômico e socioambiental; Gestão Ambiental; Espeleoturismo e Uso Público.
5. Definir explicitamente a política para registros antigos (subárea nula) e para exclusão de uma área/subárea vinculada: preservar `PROTECT` e informar os registros bloqueadores.

### 2. CRUD administrativo

1. Criar `SubAreaTematicaForm` em `apps/repositorio/forms/metadados_forms.py`, com select da área temática existente, nome e status. A relação de subáreas será obrigatória ao criar novos registros, mas a edição deverá continuar permitindo registros legados sem subárea.
2. Implementar `SubAreaTematicaList/Create/Update/DeleteView` em `metadados_views.py`, reaproveitando as classes base, incluindo busca por nome/área e filtro por ativo.
3. Adicionar as quatro rotas em `apps/repositorio/urls.py`.
4. Criar template de listagem próprio (colunas área, grupo, nome, situação e ações); reutilizar `metadado_form.html` para criar/editar e `metadado_confirm_delete.html` para exclusão.
5. Incluir “Subáreas Temáticas” no menu de Gestão.
6. Exibir a subárea no Django Admin e adicionar filtro por área/grupo/situação.
7. Atualizar o mapeamento de dependências em `BaseMetadataDeleteView` para impedir exclusão de subárea vinculada a registros e manter mensagens de erro úteis.

### 3. Cadastro e apresentação de registros

1. Incluir `subarea_tematica` no `RegistroForm`, labels/widgets, querysets ativos e testes.
2. Disponibilizar todas as subáreas ativas no formulário, agrupadas/ordenadas por área temática, sem carregamento dinâmico ou endpoint JSON.
3. Garantir validação server-side da consistência área/subárea, inclusive em POST manipulado, e exigir ao menos uma subárea em novos registros.
4. Mostrar a subárea no formulário de registro e no detalhe público/administrativo.
5. Atualizar importadores (`www/django_code/carga_publicacaoes.py`) e qualquer carga SQL/fixture para aceitar o novo metadado sem apagar dados existentes.

### 4. Busca avançada pública

1. Adicionar `subareas_tematicas` ao `RepositorioFilterForm`, com label “Subárea Temática”, opções ativas e ordenação por área/nome.
2. Aplicar o parâmetro em `filter_repository_queryset` usando a relação ManyToMany do registro; manter compatibilidade quando o parâmetro estiver ausente ou vazio.
3. Incluir o campo no template `repository_advanced_filters.html`.
4. Incluir o nome do campo na lista de filtros ativos e no estado visual de busca em `repo_busca.html`, preservando os parâmetros ao limpar, paginar, editar e baixar resultados.
5. Revisar a função de download/listagem administrativa que replica filtros, para que o resultado exportado seja idêntico ao resultado exibido.
6. Usar `prefetch_related('subareas_tematicas__area_tematica')` onde a listagem exibe os valores, evitando consultas adicionais.

## Testes e critérios de aceite

- Testes de modelo: criação, unicidade por área, grupos válidos, relação área/subárea e proteção contra exclusão com registros vinculados.
- Testes de formulário: campos obrigatórios/opcionais, querysets ativos e rejeição de subárea pertencente a outra área.
- Testes de views do CRUD: autenticação, listagem/paginação/busca, criação, edição, exclusão protegida e mensagens.
- Testes de registros: persistência, edição, detalhe e compatibilidade de registros sem subárea.
- Testes da busca: cada subárea retorna somente seus registros; ausência do filtro não muda o resultado; combinação com área temática, projeto, status e ordenação; estado do filtro no template e download.
- Verificação manual responsiva: menu de Gestão, CRUD, formulário de registro e Busca Avançada em desktop/mobile.
- Executar migrações e a suíte direcionada existente (`apps/repositorio/tests`); depois rodar a suíte completa se os testes direcionados passarem.

## Sequência sugerida de entrega

1. Modelos, migrações e seed.
2. CRUD/admin/menu de subáreas.
3. Integração da subárea ao `Registro` e aos importadores.
4. Filtro público e download/listagens.
5. Testes automatizados, revisão visual e documentação operacional.

## Pontos a confirmar antes de codificar

As decisões foram definidas:

1. Um `Registro` pode possuir várias subáreas (ManyToMany).
2. A subárea é obrigatória para novos registros, mas registros existentes podem permanecer sem subárea.
3. As nove opções informadas serão criadas automaticamente como carga inicial fixa.
