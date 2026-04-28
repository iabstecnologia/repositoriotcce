import json
from collections import defaultdict

# Caminho para o seu arquivo
json_file = 'carga_json.json'

with open(json_file, 'r', encoding='utf-8-sig') as f:
    dados = json.load(f)

# Dicionário para armazenar os títulos e os índices em que aparecem
titulos_encontrados = defaultdict(list)

for index, item in enumerate(dados):
    # Usamos o título como chave (removendo espaços extras para garantir a comparação)
    titulo = item.get('TITULO', '').strip()
    titulos_encontrados[titulo].append(index + 1) # +1 porque a lista começa em 0

print("--- RELATÓRIO DE DUPLICATAS ---")
for titulo, posicoes in titulos_encontrados.items():
    if len(posicoes) > 1:
        print(f"\nTítulo: {titulo}")
        print(f"Aparece nos objetos de índice: {posicoes}")