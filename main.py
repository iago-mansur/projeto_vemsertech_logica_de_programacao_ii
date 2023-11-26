import json
from functools import reduce

def visualizar_dados(base):

    for restaurante in base:
        print("-----------------------------")
        print("nome:", restaurante["nome"])
        print("prato:", restaurante["prato"])
        print("preco:", restaurante["preco"])
        print("-----------------------------")

def dados_unico_restaurante(base):
        
        print("Nome dos restaurantes:\n", list(map(lambda b: b["nome"], base)))
        
        dados_unico = input("Informe o restaurante:").lower()

        lista_filtro = filtrar_restaurante(base, dados_unico)
        
        print("Dados do restaurante selecionado:\n", lista_filtro)

def atualizar_restaurante(base):
    
    i = indice_restaurante(base)
    dados_atual = dados_novos()

    base[i] = dados_atual
    
    gravar_dados_json(base)

def adicionar_restaurante(base):
    
    dados_add = dados_novos()
    base.append(dados_add)
    gravar_dados_json(base)

def remover_restaurante(base):
    
    i = indice_restaurante(base)
    base.pop(i)
    gravar_dados_json(base)

def listar_estatisticas(base):
    
    media = valor_medio_prato(base)
    mini = getMinMax(base)
    maxi = getMinMax(base, get_min = False)
    gravar_dados_csv(media, mini, maxi)
    
    print(f"O preço médio é {media: .2f}, os dados do prato de menor valor são: {mini}, e os dados do prato de maior valor são: {maxi}")

def filtrar_restaurante(base, dados):           

    return list(filter(lambda i: i['nome'].lower() == dados, base))

def indice_restaurante(base):
    
    print("Nomes dos restuarntes: ", list(map(lambda b: b["nome"] , base)))
    
    return int(input("Informe o indice do retaurante: "))

def dados_novos():
    
    nome = input("Digite o nome do restaurante: ").lower()

    prato = input("Digite o prato do restaurante: ").lower()

    preco = float(input("Digite o preço: "))
    
    dados_novos = {
        'nome': nome,
        'prato': prato,
        'preco': preco
    }

    return dados_novos

def valor_medio_prato(base):
    
    total_pratos = len(base)
    preco_medio = reduce(lambda soma, b: soma + b["preco"], base, 0)/total_pratos
    
    return preco_medio

def getMinMax(base= [], get_min= True):
  
  try:
    
    num_min_max = base[0]["preco"]
    lista_min_max = [(base[0]["prato"], base[0]["preco"])]
    
    for i in range(1, len(base)):
      
      if get_min:
        
        if base[i]["preco"] < num_min_max:
          num_min_max = base[i]["preco"]
          lista_min_max = [(base[i]["prato"], base[i]["preco"])]

        elif num_min_max == base[i]["preco"]:
            lista_min_max.append((base[i]["prato"], base[i]["preco"]))
      
      else:
        
        if base[i]["preco"]  > num_min_max:
          num_min_max = base[i]["preco"]
          lista_min_max = [(base[i]["prato"], base[i]["preco"])]
        
        elif num_min_max == base[i]["preco"]:
            lista_min_max.append((base[i]["prato"], base[i]["preco"]))

    return lista_min_max
  
  except IndexError:
    
    return "Lista vazia!"

def ler_dados():
    
    try:
        
        with open("base.json", encoding="utf-8", mode="r") as arq:

            json_string = arq.read()
            base = json.loads(json_string)

    except:

        print('Erro!')

    return base


def gravar_dados_json(base):

    try:
        
        with open("base.json", encoding="utf-8", mode="w") as arq:
            arq.write(json.dumps(base))
    
    except:

        print('Erro!')


def gravar_dados_csv(media, mini, maxi):

    try:
        
        with open("estatisticas.csv", encoding="utf-8", mode="w") as arq:
            arq.write(f"{media}, {mini}, {maxi},\n")

    except:

        print('Erro!')

def menu():
    
    menu = '''
    ---------- Menu ----------

    [0] - Finalizar

    [1] - Visualizar Dados

    [2] - Exibir Restaurante selecionado

    [3] - Atualizar Restaurante

    [4] - Adicionar Restaurante

    [5] - Remover restaurante

    [6] - Estatísticas dos restaurantes

    --------------------
    '''
    
    return input(menu)


def main():

    base = ler_dados()
    controle_main = True

    while controle_main:
    
        opcao = menu()
        
        if opcao == '1':
            print("Segue a lista atualizada de restaurantes:\n")
            visualizar_dados(base)
            
        elif opcao == '2':
            dados_unico_restaurante(base)

        elif opcao == '3':
            atualizar_restaurante(base)

        elif opcao == '4':
            adicionar_restaurante(base)
        
        elif opcao == '5':
            remover_restaurante(base)

        elif opcao == '6':
            listar_estatisticas(base)
        
        elif opcao == '0':
            print('App Encerrado.')
            controle_main = False  
        
        else:
            print('Opção Inválida')



main()
