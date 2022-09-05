from functionsAG import Listar_Contato
from functionsAG import Buscar_Contato
from functionsAG import Cadastrar_Contato
from functionsAG import Deletar_Contato
from functionsAG import sair_do_programa




def menu():
    voltaraomenu = 'y'
    while voltaraomenu == 'y':
        opcao = input('''Menu
        [1] Listar Contatos
        [2] Cadastrar Contato
        [3] Deletar Contato
        [4] Buscar Contato Pelo ID 
        [5] Sair
        ''')
        
        if opcao == '1':
            Listar_Contato()
        elif opcao == '2':
            Cadastrar_Contato()
        elif opcao == '3':
            Deletar_Contato()
        elif opcao == '4':
            Buscar_Contato()
        else:
            print('Você optou por sair do programa.')
            sair_do_programa()   

    voltaraomenu = input('Deseja voltar ao menu principal (y/n)').lower



def main():
    menu()
main()
