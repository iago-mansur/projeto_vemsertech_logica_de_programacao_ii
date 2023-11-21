import json



def visualizar_dados():
  
  base = ler_dados()

  print ("Os dados atuais são: " + str(base))


def exibir_restaurante():
    
    print(procurar_restaurante())


def atualizar_restaurante():
    
    x = procurar_restaurante()

    print(x)
    
    dados = dict(input("Dados do dicionario atualizado:"))
    print(dados)
    """
    print(nome)
    print(type(nome))
    prato = input("Prato atualizado:")
    print(prato)
    print(type(prato))
    valor = float(input("valor atualizado:"))
    print(valor)
    print(type(valor))
    dados = dict(zip(nome, prato, valor))
    print(dados)       
    """

    #base = ler_dados()

    #base.update(dados)

    #gravar_dados(dados)


def adicionar_restaurante():
    pass
"""
lambda
return map(gravar_dados, ('a', 'b', 'c')) 
"""

def remover_restaurante():
    
    base = ler_dados()

    dados = procurar_restaurante()

    base_atualizada = [i for i in base if i['nome'] != dados["nome"]]
    
    print(base_atualizada)

    """
    dados = input("Informe o restaurante:").lower()
    
    base = ler_dados()             
    
   
    return   list(filter(lambda i: i['nome'].lower() != dados, base))
    """
    """   
    def remover_lista(x):
        return filter(lambda i: i['nome'] not in x['nome'], y)
    removedor = remover_lista(dados)
    list(map(removedor,base))
    """
    
    """
    base = ler_dados()

    dados = procurar_restaurante()
    
    base_atual = [i for n, i in enumerate(base) if i not in dados.itens()]
    

    print(base_atual)
    """
    """
    gravar_dados(base_atual)
    
    visualizar_dados()

    def filtro_dados(x):
        for dados in 
        x["name"] = dados["dados"]
"""

def ler_dados():
    
    try:
        
        with open("base.json", encoding="utf-8", mode="r") as arq:

            json_string = arq.read()
            base = json.loads(json_string)

    except:

        print('Erro!')

    return base


def gravar_dados():
    pass


def procurar_restaurante():

    dados = input("Informe o restaurante:").lower()
    
    base = ler_dados()             
    
    return list(filter(lambda i: i['nome'].lower() == dados, base)) 

def menu():
    
    menu = '''
    ---------- Menu ----------

    [0] - Finalizar

    [1] - Visualizar Dados

    [2] - Exibir Restaurante

    [3] - Atualizar Restaurante

    [4] - Adicionar Restaurante

    [5] - Remover restaurante

    --------------------
    '''
    
    return input(menu)


def main():

    controle_main = True

    while controle_main:
    
        opcao = menu()
        
        if opcao == '1':
            visualizar_dados()

        elif opcao == '2':
            exibir_restaurante()
        
        elif opcao == '3':
            atualizar_restaurante()

        elif opcao == '4':
            adicionar_restaurante()
        
        elif opcao == '5':
            remover_restaurante()
        
        elif opcao == '0':
            print('App Encerrado.')
            controle_main = False  
        
        else:
            print('Opção Inválida')



main()
