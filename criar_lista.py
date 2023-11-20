import json

base = [
    {
        'nome': 'Restaurante1',
        'prato': 'Prato1',
        'preco': 11.11
    },
    {
        'nome': 'Restaurante2',
        'prato': 'Prato2',
        'preco': 22.22
    },
    {
        'nome': 'Restaurante3',
        'prato': 'Prato3',
        'preco': 33.33
    }
]

string_json = json.dumps(base)

with open("base.json", encoding="utf-8", mode="w") as arq:
    arq.write(json.dumps(base))