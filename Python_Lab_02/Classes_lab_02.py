import pyodbc
import pandas as pd
from os import system

server = '-------------------------------'
driver = '-------------------------------'
database = '-------------------'
username = '------------------------'
Authentication = '------------------------------'
port = '----------------------'

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
                       '{self.email}','{self.bairro}', '{self.nascimento}') "
        cursor.execute(novo_usuario)
        cursor.commit()


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
                      '{self.creditos}','{self.tipocartao}', '{self.emissao}' )"
        cursor.execute(novo_cartao)
        cursor.commit()


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
                   '{self.modelobus}','{self.anofabrica}', '{self.id_motorista}') "
        cursor.execute(novo_bus)
        cursor.commit()


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
                         '{self.sobrenome}', '{self.nascimento}') "
        cursor.execute(novo_motorista)
        cursor.commit()
