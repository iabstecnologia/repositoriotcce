# Repopulação do Repositório

O comando único `repopular_repositorio` concentra a validação, limpeza, carga de referências e importação dos registros.

## Proteções

- O banco deve ser PostgreSQL.
- Usuários e tabelas de autenticação são preservados.
- `FotoGaleria` e arquivos de mídia local/S3 são preservados.
- O comando não usa `flush`.
- Referências são resolvidas por nomes, sem depender dos IDs do banco de origem.
- Faça `pg_dump` e backup da mídia antes de executar a operação destrutiva.

## Repopulação

Primeiro valide sem alterar o banco:

```bash
python manage.py repopular_repositorio --dry-run
```

A validação confirma PostgreSQL, migrations aplicadas, usuário de auditoria, JSON válido com `457` itens e os arquivos SQL/JSON de carga disponíveis.

Depois de conferir o backup e o ambiente, execute:

```bash
python manage.py repopular_repositorio --apply --confirm-repopulate
```

A operação é transacional e:

1. Remove vínculos Many-to-Many de registros.
2. Remove `Registro`.
3. Preserva `FotoGaleria`.
4. Remove subprojetos, projetos, autores, tags e demais referências do app.
5. Recria as referências a partir de `www/sql_carga/carga_inicial.sql` e do JSON.
6. Ajusta as sequências PostgreSQL.
7. Importa os `457` registros de `www/json_carga/carga_json.json`.
8. Recria os vínculos de autores e tags.
9. Mantém os `4` projetos e `176` subprojetos definidos no SQL, incluindo `TCCE 3/2026`.

Datas nos formatos `MM/YYYY` e `DD/MM/YYYY` são aceitas. URLs HTTP são gravadas em `link_externo`.

Os nomes dos subprojetos já foram incorporados ao JSON a partir dos CSVs. A repopulação não executa uma etapa de sincronização separada.

Os CSVs da raiz são usados apenas para auditoria e geração da carga. Eles não são necessários para executar a repopulação.

O projeto `TCCE 1/2020` foi removido da carga inicial.

## Validação Final

Após a carga, confirme:

```bash
python manage.py check
python manage.py showmigrations --plan
python manage.py test apps.repositorio
```

O resultado esperado é:

- `457` registros.
- Nenhum registro sem autor ou tag.
- Usuários preservados.
- Vínculos `registro_autores` e `registro_tags` recriados.
- As referências `SUBPROJETO 22 (AÇÃO 4.23)`, `GISELLE RIBEIRO`, `CURSO`, `PAN CAVERNAS` e `LICENCIAMENTO` presentes.

## Fontes De Dados

- `www/json_carga/carga_json.json`: registros do acervo.
- `www/sql_carga/carga_inicial.sql`: fonte única dos projetos, subprojetos e demais referências iniciais.
- CSVs da raiz: auditoria e geração da carga, sem participação no fluxo de produção.
- `apps/repositorio/management/commands/repopular_repositorio.py`: implementação do fluxo único.
