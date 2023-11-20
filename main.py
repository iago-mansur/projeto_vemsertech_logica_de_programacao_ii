import json



def visualizar_restaurantes():
  print(base)
  print(type(base))


def exibir_restaurante():
  pass


def atualizar_restaurante():
  pass


def adicionar_restaurante():
    pass


def remover_restaurante():
    pass


def menu():
    
    menu = '''
    ---------- Menu ----------

    [0] - Finalizar

    [1] - Visualizar Restaurantes

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
            visualizar_restaurantes()

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

with open("base.json") as arq:

    json_string = arq.read()
    base = json.loads(json_string)

main()
