# Sincronização dos subprojetos TCCE

O comando `sincronizar_subprojetos_tcce` lê os arquivos `Lista de Projetos TCCE*.csv` na raiz do repositório e sincroniza os dados com o banco configurado no Django.

Para cada linha, a identificação é feita por:

```text
TCCE/projeto + código do subprojeto
```

Essa chave evita misturar subprojetos com o mesmo número em TCCEs diferentes.

O comando:

- atualiza o nome de subprojetos existentes;
- cria subprojetos ausentes;
- cria o projeto-pai quando ele ainda não existe;
- não altera os vínculos existentes entre registros e subprojetos;
- executa as gravações dentro de uma transação;
- rejeita linhas duplicadas ou códigos ambíguos.

## Validação

Sem argumentos, o comando apenas valida os CSVs e mostra o resumo das alterações. Nenhum dado é gravado:

```bash
python manage.py sincronizar_subprojetos_tcce
```

Na validação realizada, foram identificados:

- 68 subprojetos para atualização;
- 1 projeto novo: `TCCE 3/2026`;
- 108 subprojetos novos.

## Aplicação

Antes de aplicar, confirme que o Django está apontando para o banco correto e faça um backup. A opção `--apply` grava as alterações no banco configurado:

```bash
python manage.py sincronizar_subprojetos_tcce --apply
```

A migration que amplia `Subprojeto.nome` para 255 caracteres deve ser aplicada antes da sincronização:

```bash
python manage.py migrate repositorio
```

Em caso de erro durante a gravação, a transação é revertida e a execução não deixa inclusões parciais.
