import pyodbc
import pandas as pd
from os import system


server = 'sql-estudo.database.windows.net'
driver = '{ODBC Driver 17 for SQL Server}'
database = 'db-estudos'
username = 'pedro.canizela@blueshift.com.br'
Authentication = 'ActiveDirectoryInteractive'
port = '1433'

conn = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';AUTHENTICATION='+Authentication+';PORT='+port+';DATABASE='+database+';UID='+username)#+';PWD='+password)


cursor = conn.cursor()


class Usuario:
    def __init__(self, nome=str, sobrenome=str, email=str, bairro=str, nascimento='nascimento'):
        self.nome = nome
        self.sobrenome = sobrenome
        self.email = email
        self.bairro = bairro
        self.nascimento = nascimento

    def get_usuario(self):
        return self.nome, self.sobrenome, self.email, self.bairro, self.nascimento

    def set_usuario(self, novo_nome, novo_sobrenome, novo_email, novo_bairro, nova_data):

        self.nome = novo_nome
        self.sobrenome = novo_sobrenome
        self.email = novo_email
        self.bairro = novo_bairro
        self.nascimento = nova_data
        novo_usuario = f"INSERT INTO [PEDRO_CANIZELA_USUARIO] VALUES ('{self.nome}', '{self.sobrenome}', \
                       '{self.email}','{self.bairro}', '{self.nascimento}' "
        cursor.execute(novo_usuario)
        cursor.comit()


class Cartao:

    def __init__(self, idcartao=int, idusu=int, creditos=float, tipocartao=str, emissao='emissao'):

        self.idcartao = idcartao
        self.idusu = idusu
        self.creditos = creditos
        self.tipocartao = ['comum', 'estudante', 'vale-transporte', 'idoso']
        self.emissao = emissao

    def get_cartao(self):
        return self.idcartao, self.idusu, self.creditos, self.tipocartao, self.emissao

    def set_cartao(self, novo_id_cartao, novo_idusu, novo_credito, novo_tipo, nova_emissao):

        self.idcartao = novo_id_cartao
        self.idusu = novo_idusu
        self.creditos = novo_credito
        self.tipocartao = novo_tipo
        self.emissao = nova_emissao
        novo_cartao = f"INSERT INTO [PEDRO_CANIZELA_CARTAO] VALUES ('{self.idcartao}', '{self.idusu}', \
                      '{self.creditos}','{self.tipocartao}', '{self.emissao}' "
        cursor.execute(novo_cartao)
        cursor.comit()


class Onibus:
    def __init__(self, numplaca=int, numlinha=int, modelobus=str, anofabrica='ano_fabrica', id_motorista='id_motorist'):

        self.numplaca = numplaca
        self.numlinha = numlinha
        self.modelobus = modelobus
        self.anofabrica = anofabrica
        self.id_motorista = id_motorista

    def get_onibus(self):
        return self.numplaca, self.numlinha, self.modelobus, self.anofabrica

    def set_onibus(self, nova_placa, nova_linha, novo_modelo, nova_anofrabrica, novo_id_motorista):

        self.numplaca = nova_placa
        self.numlinha = nova_linha
        self.modelobus = novo_modelo
        self.anofabrica = nova_anofrabrica
        self.id_motorista = novo_id_motorista
        novo_bus = f"INSERT INTO [PEDRO_CANIZELA_ONIBUS] VALUES ('{self.numplaca}', '{self.numlinha}', \
                   '{self.modelobus}','{self.anofabrica}', '{self.id_motorista}' "
        cursor.execute(novo_bus)
        cursor.comit()


class Motorista:
    def __init__(self, numcnh=int, nome=str, sobrenome=str, nascimento='nascimento'):

        self.numcnh = numcnh
        self.nome = nome
        self.sobrenome = sobrenome
        self.nascimento = nascimento

    def get_motorista(self):
        return self, self.numcnh, self.nome, self.sobrenome, self.nascimento

    def set_motorista(self, nova_cnh, novo_nome, novo_sobrenome, nova_data):

        self.numcnh = nova_cnh
        self.nome = novo_nome
        self.sobrenome = novo_sobrenome
        self.nascimento = nova_data
        novo_motorista = f"INSERT INTO [PEDRO_CANIZELA_MOTORISTA] VALUES ('{self.numcnh}', '{self.nome}', \
                         '{self.sobrenome}', '{self.nascimento}' "
        cursor.execute(novo_motorista)
        cursor.comit()


def menu_inicial():
    print(""" Bem Vindo ao sistema de cadastro de dados da PoccoBus,
 selecione qual açao você deseja realizar: 
    
    [1] Realizar cadastro;
    
    [2] Verificar tabelas;
    
    [3] Sair.""")

    opcao1 = int(input('>>>'))

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
    print('Esperamos ver você em breve, até logo')


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
    new_user.set_usuario(f'{nome}, {sobrenome}, {email}, {bairro}, {data_nascimento}')
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
    new_card.set_cartao(f'{id_cartao}, {id_usuario}, {creditos}, {tipo_cartao}, {data_emissao}')
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
    new_bus.set_onibus(f'{num_placa}, {num_linha}, {modelo_bus}, {ano_fabrica}, {id_motorista}')
    print('Ônibus cadastrado com sucesso, você será redirecionado para o '
          'menu inicial para decidir o que deseja realizar em seguida.')
    menu_inicial()


def cadastrar_motorista():
    new_driver = Motorista()
    cnh = int(input('Digite sua CNH >>> '))
    nome = str(input('Digite seu nome >>> '))
    sobrenome = str(input('Digite seu sobrenome >>> '))
    data_nascimento = str(input('Digite sua data de nascimrnto [YYYY-MM-DD] >>> '))
    new_driver.set_motorista(f'{cnh}, {nome}, {sobrenome}, {data_nascimento}')
    print('Motorista cadastrado com sucesso, você será redirecionado para o '
          'menu inicial para decidir o que deseja realizar em seguida.')
    menu_inicial()


menu_inicial()
