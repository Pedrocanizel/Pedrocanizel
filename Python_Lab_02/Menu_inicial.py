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

def menu_inicial():
    print(""" Bem Vindo ao sistema de cadastro de dados da PoccoBus,
 selecione qual açao você deseja realizar: 
    
    [1] Realizar cadastro;
    
    [2] Verificar tabelas;
    
    [3] Sair.""")


    opçao1 = int(input('>>>'))

    if opçao1 == 1:
        exit()

    elif opçao1 == 2:
        menu_de_escolher_tabela()

    elif opçao1 == 3:
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


menu_inicial()
