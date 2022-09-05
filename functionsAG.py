from ast import NotIn


def Cadastrar_Contato():
    id_cadastro = input('Número de Identificação ')
    nome_cadastro = input('Nome do Contato ')
    email_cadastro = input('E-mail do usúario ')
    numero_cadastro = input('Número do Usúario')
    
    try:
        arquivo_agenda = open('agenda.txt', 'a')
        dados_contato = f'{id_cadastro};{nome_cadastro};{email_cadastro};{numero_cadastro}\n'
        arquivo_agenda.write(dados_contato)
        arquivo_agenda.close()
        print('Contato Gravado com sucesso!') 
    except:
        print('ERRO ao Cadastrar Contato ')



def Listar_Contato():
    agenda = open('agenda.txt','r')
    for contato in agenda:
        print(contato)
    agenda.close()
    


def Deletar_Contato():
    Deletar_nome = input('Contato que deseja deletar: ')
    agenda = open('agenda.txt','r')
    aux = []
    aux2 = []

    for i in agenda:
        aux.append(i)
    for i in range (0, len(aux)):
        if Deletar_nome not in aux[i]:
            aux2.append(aux[i])
    agenda = open('agenda.txt','w')
    for i in aux2:
        agenda.write(i)
    print('Contato deletado com sucesso! ')
    Listar_Contato()



def Buscar_Contato():
    nome = input('Nome do Contato Desejado: ')
    agenda = open('agenda.txt','r')
    for contato in agenda:
        if nome in (contato.split(';')[0]):
            print(contato)        
        elif nome not in agenda: 
            print('ERRO ao localizar contato!')



def sair_do_programa():
    exit()
