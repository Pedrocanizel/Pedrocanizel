from Classes_lab_02 import *
from os import system


def menu_inicial():
    print("""    \033[1;36m\U0001F683 \U0001F683 \U0001F683 \U0001F683 \U0001F683 \U0001F683 \U0001F683
    \U0001F683               \U0001F683
    \U0001F683               \U0001F683
    \U0001F683               \U0001F683
    \U0001F683 \U0001F683 \U0001F683 \U0001F683 \U0001F683 \U0001F683 \U0001F683
    \U0001F683               
    \U0001F683
    \U0001F683
    \U0001F683

    \033[1;35m\U0001F683 \U0001F683 \U0001F683 \U0001F683 \U0001F683 \U0001F683 \U0001F683
    \U0001F683               \U0001F683
    \U0001F683               \U0001F683
    \U0001F683               \U0001F683
    \U0001F683 \U0001F683 \U0001F683 \U0001F683 \U0001F683 \U0001F683 \U0001F683
    \U0001F683               \U0001F683      
    \U0001F683               \U0001F683
    \U0001F683               \U0001F683
    \U0001F683 \U0001F683 \U0001F683 \U0001F683 \U0001F683 \U0001F683 \U0001F683
    """)
    print("""\033[1;32mBEM VINDO AO SISTEMA DE CADASTRO DA POCCOBUS,
 SELECIONE QUAL AÇAO VOCÊ DESEJA REALIZAR: 
    
    \033[1;33m[1] Realizar cadastro;
    
    \033[1;34m[2] Verificar tabelas;
    
    \033[1;31m[3] Sair.""")

    opcao1 = int(input('\033[1;31m>>>'))

    if opcao1 == 1:
        print('Qual cadastro você deseja realizar?')
        print(""" 
        [1] Cadastrar novo usuário;
        
        [2] Cadastrar novo cartao;
        
        [3] Cadastrar novo ônibus;
        
        [4] Cadastrar novo motorista;
        
        [5] Retornar ao menu inicial.
        """)

        cadastro = int(input('>>>'))

        if cadastro == 1:
            cadastrar_usuario()

        elif cadastro == 2:
            cadastrar_cartao()

        elif cadastro == 3:
            cadastrar_onibus()

        elif cadastro == 4:
            cadastrar_motorista()

        elif cadastro == 5:
            menu_inicial()

        else:
            print('Você digitou um valor INVÁLIDO e será redirecionado ao menu inicial para decidir o que fazer.')
            menu_inicial()

    elif opcao1 == 2:
        menu_de_escolher_tabela()

    elif opcao1 == 3:
        mensagem_sair()
        exit()

    else:
        print('Você digitou uma opçao INVÁLIDA')
        menu_inicial()


def mensagem_sair():
    print('\033[1;36mEsperamos ver você em breve, até logo')


def ver_tabela_usuario():

    ver_usuario = pd.read_sql("SELECT * FROM [dbo].[PEDRO_CANIZELA_USUARIO];", conn)
    df = pd.DataFrame(ver_usuario)
    df2 = df.to_string(index=False)
    system('cls')
    print(df2)
    print('Agora selecione a opçao que você deseja: ')
    menu_de_escolher_tabela()


def ver_tabela_cartao():

    ver_cartao = pd.read_sql("SELECT * FROM [dbo].[PEDRO_CANIZELA_CARTAO];", conn)
    df = pd.DataFrame(ver_cartao)
    df2 = df.to_string(index=False)
    system('cls')
    print(df2)
    print('Agora selecione a opçao que você deseja: ')
    menu_de_escolher_tabela()


def ver_tabela_motorista():

    ver_motorista = pd.read_sql("SELECT * FROM [dbo].[PEDRO_CANIZELA_MOTORISTA];", conn)
    df = pd.DataFrame(ver_motorista)
    df2 = df.to_string(index=False)
    system('cls')
    print(df2)
    print('Agora selecione a opçao que você deseja: ')
    menu_de_escolher_tabela()


def ver_tabela_onibus():

    ver_onibus = pd.read_sql("SELECT * FROM [dbo].[PEDRO_CANIZELA_ONIBUS];", conn)
    df = pd.DataFrame(ver_onibus)
    df2 = df.to_string(index=False)
    system('cls')
    print(df2)
    print('Agora selecione a opçao que você deseja: ')
    menu_de_escolher_tabela()


def menu_de_escolher_tabela():
    print("""Qual tabela você deseja ver?

            [1] USUÁRIOS
            [2] CARTAO
            [3] MOTORISTA
            [4] ÔNIBUS
            [5] VOLTAR PARA O MENU INICIAL
            """)
    tabela = int(input('>>>'))
    if tabela == 1:
        ver_tabela_usuario()

    elif tabela == 2:
        ver_tabela_cartao()

    elif tabela == 3:
        ver_tabela_motorista()

    elif tabela == 4:
        ver_tabela_onibus()

    elif tabela == 5:
        menu_inicial()

    else:
        print('Opçao INVÁLIDA, escolha uma tabela para ver ou volte '
              'para o menu inicial')
        menu_de_escolher_tabela()


def cadastrar_usuario():
    new_user = Usuario()
    nome = str(input('Digite seu nome >>> '))
    sobrenome = str(input('Digite seu sobrenome >>> '))
    email = str(input('Digite seu email >>> '))
    bairro = str(input('Digite seu bairro >>> '))
    data_nascimento = str(input('Digite sua data de nascimrnto [YYYY-MM-DD] >>> '))
    new_user.set_usuario(nome, sobrenome, email, bairro, data_nascimento)
    print('Usuário cadastrado com sucesso, você será redirecionado para o '
          'menu inicial para decidir o que deseja realizar em seguida.')
    menu_inicial()


def cadastrar_cartao():
    new_card = Cartao()
    id_cartao = int(input('Digite o ID do seu cartao >>> '))
    id_usuario = int(input('Digite seu ID de usuário >>> '))
    creditos = float(input('Digite quantos créditos você deseja inserir >>> '))
    perg_tipo_cartao = int(input("""Qual é o tipo do seu cartao?

    [1] Comum
    [2] Estudante
    [3] Vale-transporte
    [4] Idoso

    >>> """))
    if perg_tipo_cartao == 1:
        tipo_cartao = 'comum'
    elif perg_tipo_cartao == 2:
        tipo_cartao = 'estudante'
    elif perg_tipo_cartao == 3:
        tipo_cartao = 'vale-transporte'
    elif perg_tipo_cartao == 4:
        tipo_cartao = 'idoso'
    else:
        print('Você digitou um valor inválido, preste mais atençao')
        cadastrar_cartao()
    data_emissao = str(input('Digite a data de emissao do seu cartao [YYYY-MM-DD] >>> '))
    new_card.set_cartao(id_cartao, id_usuario, creditos, tipo_cartao, data_emissao)
    print('Cartao cadastrado com sucesso, você será redirecionado para o '
          'menu inicial para decidir o que deseja realizar em seguida.')
    menu_inicial()


def cadastrar_onibus():
    new_bus = Onibus()
    num_placa = int(input('Digite o número da placa >>> '))
    num_linha = int(input('Digite o número da linha >>> '))
    modelo_bus = str(input('Digite o modelo do ônibus >>> '))
    ano_fabrica = str(input('Digite a data de fabricacao [YYYY-MM-DD] >>> '))
    id_motorista = int(input('Digite seu número de identificaçao >>> '))
    new_bus.set_onibus(num_placa, num_linha, modelo_bus, ano_fabrica, id_motorista)
    print('Ônibus cadastrado com sucesso, você será redirecionado para o '
          'menu inicial para decidir o que deseja realizar em seguida.')
    menu_inicial()


def cadastrar_motorista():
    new_driver = Motorista()
    cnh = int(input('Digite sua CNH >>> '))
    nome = str(input('Digite seu nome >>> '))
    sobrenome = str(input('Digite seu sobrenome >>> '))
    data_nascimento = str(input('Digite sua data de nascimrnto [YYYY-MM-DD] >>> '))
    new_driver.set_motorista(cnh, nome, sobrenome, data_nascimento)
    print('Motorista cadastrado com sucesso, você será redirecionado para o '
          'menu inicial para decidir o que deseja realizar em seguida.')
    menu_inicial()


menu_inicial()
