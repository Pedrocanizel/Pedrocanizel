import requests
import pandas as pd
from conexao_bd_lab_02_azure import *


def buscar_api():
    url = 'https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/CotacaoDolarPeriodo(dataInicial' \
          '=@dataInicial,dataFinalCotacao=@dataFinalCotacao)?@dataInicial=%2701-01-2019%27&@dataFinal' \
          'Cotacao=%2712-31-2025%27&$top=9000&$format=text/csv&$select=cotacaoCompra,cotacaoVenda,dataHoraCotacao'

    get_api = requests.get(url).content.decode('utf-8')
    with open('dados_dolar_az02.csv', 'w') as new_csv:
        new_csv.write(get_api)

def ler_arquivo():
    ler_com_pandas = pd.read_csv('dados_dolar_az02.csv')
    ler_com_pandas = ler_com_pandas.values.tolist()
    cursor.execute('TRUNCATE TABLE [DOLAR_PEDRO_CANIZELA.DOLAR_STAGE_PEDRO_CANIZELA]')
    #cursor.commit()
    into_sql = "INSERT INTO [DOLAR_PEDRO_CANIZELA.DOLAR_STAGE_PEDRO_CANIZELA] VALUES (?,?,?)"
    cursor.fast_executemany = True
    cursor.executemany(into_sql, ler_com_pandas)
    cursor.commit()
    cursor.close()
    conn.close()

buscar_api()
ler_arquivo()
