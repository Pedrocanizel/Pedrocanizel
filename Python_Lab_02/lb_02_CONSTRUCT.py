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



#cursor.execute(ver_tabelas)

#def inserir_usuario():
#    INSERT INTO[dbo].[PEDRO_CANIZELA_USUARIO](
#        NOME_USUARIO, SOBRENOME_USUARIO, EMAIL, BAIRRO, DATA_NASCIMENTO
# VALUES ('Pedro', 'Canizela' , 'pedro.canizela@gmail.com', 'CIC', '19920328')

#def inserir_cartao():
#    INSERT
#    INTO[dbo].[PEDRO_CANIZELA_CARTAO](
#        QUANTIDADE_DE_CREDITOS, TIPO_CARTAO, DATA_EMISSAO)
#    VALUES('Pedro', 'Canizela', 'pedro.canizela@gmail.com', 'CIC', '19920328')

#def inserir_motorista():
 #   INSERT
#    INTO[[dbo].[PEDRO_CANIZELA_MOTORISTA]]] (
#    NUMERO_CNH, NOME_MOTORISTA, SOBRENOME_MOTORISTA, DATA_NASCIMENTO)
#    VALUES('Pedro', 'Canizela', 'pedro.canizela@gmail.com', 'CIC', '19920328')

#def inserir_onibus():
#    INSERT
 #   INTO[dbo].[PEDRO_CANIZELA_ONIBUS](
 #       NUMERO_PLACA, NUMERO_LINHA, MODELO_ONIBUS, ANO_FABRICACAO)
#    VALUES(......)


def ver_tabela_usuario():

    ver_usuario = pd.read_sql("SELECT * FROM [dbo].[PEDRO_CANIZELA_USUARIO];", conn)
    df = pd.DataFrame(ver_usuario)
    df2 = df.to_string(index=False)
    system('cls')
    print(df2)

def ver_tabela_cartao():

    ver_cartao = pd.read_sql("SELECT * FROM [dbo].[PEDRO_CANIZELA_CARTAO];", conn)
    df = pd.DataFrame(ver_cartao)
    df2 = df.to_string(index=False)
    system('cls')
    print(df2)

def ver_tabela_motorista():

    ver_motorista = pd.read_sql("SELECT * FROM [dbo].[PEDRO_CANIZELA_MOTORISTA];", conn)
    df = pd.DataFrame(ver_motorista)
    df2 = df.to_string(index=False)
    system('cls')
    print(df2)

def ver_tabela_onibus():

    ver_onibus = pd.read_sql("SELECT * FROM [dbo].[PEDRO_CANIZELA_ONIBUS];", conn)
    df = pd.DataFrame(ver_onibus)
    df2 = df.to_string(index=False)
    system('cls')
    print(df2)

ver_tabela_usuario()
ver_tabela_cartao()
ver_tabela_onibus()
ver_tabela_motorista()
