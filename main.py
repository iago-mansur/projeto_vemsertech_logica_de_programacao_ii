import json

def visualizar_dados(base):

    for restaurante in base:
        print("-----------------------------")
        print("nome:", restaurante["nome"])
        print("prato:", restaurante["prato"])
        print("preco:", restaurante["preco"])
        print("-----------------------------")

def exibir_restaurante(base):
    
    dados = input("Informe o restaurante:").lower()            

    return list(filter(lambda i: i['nome'].lower() == dados, base))

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


def gravar_dados_csv(base):

    try:
        
        with open("base.csv", encoding="utf-8", mode="w") as arq:

            cont = 0        

            for restaurante in base:
                print(restaurante)
                if cont == 0:
                    arq.write("nome, prato, preco \n")
                    cont += 1
                arq.write(f"{restaurante['nome']}, {restaurante['prato']}, {restaurante['peco']},\n")
    
    except:

        print('Erro!')

def menu():
    
    menu = '''
    ---------- Menu ----------

    [0] - Finalizar

    [1] - Visualizar Dados

    [2] - Exibir Restaurante

    [3] - Atualizar Restaurante

    [4] - Adicionar Restaurante

    [5] - Remover restaurante

    [6] - Exportar dados em csv

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
            print("Nome dos restaurantes:\n", list(map(lambda b: b["nome"], base)))
            lista_dados_selecionados = list(map(exibir_restaurante, base))
            print(type(lista_dados_selecionados))
            print("Dados do restaurante selecionado:\n") 
            visualizar_dados(lista_dados_selecionados)
            #("Dados do restaurante selecionado:\n", list(map(exibir_restaurante, base)))

        elif opcao == '3':
            atualizar_restaurante(base)

        elif opcao == '4':
            adicionar_restaurante(base)
        
        elif opcao == '5':
            remover_restaurante(base)
        
        elif opcao == '6':
            gravar_dados_csv(base)
        
        elif opcao == '0':
            print('App Encerrado.')
            controle_main = False  
        
        else:
            print('Opção Inválida')



main()
