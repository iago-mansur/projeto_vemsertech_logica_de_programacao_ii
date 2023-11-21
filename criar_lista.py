import json

base = [
    {
        'nome': 'restaurante1',
        'prato': 'prato1',
        'preco': 11.11
    },
    {
        'nome': 'restaurante2',
        'prato': 'prato2',
        'preco': 22.22
    },
    {
        'nome': 'restaurante3',
        'prato': 'prato3',
        'preco': 33.33
    }
]

string_json = json.dumps(base)

with open("base.json", encoding="utf-8", mode="w") as arq:
    arq.write(json.dumps(base))