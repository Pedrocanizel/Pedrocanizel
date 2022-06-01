import datetime
import pyodbc

dados_conexao = (
    "Driver=----------------------;"
    "Server=----------------------;"
    "Database=-----------------------;"
    "username=--------------------;"
    "password=------------------------------;"
)

conexao = pyodbc.connect(dados_conexao)
print("conexao bem sucedida")


class Usuario:
    def __init__(self, nome=str, sobrenome=str, email=str, bairro=str, nascimento='nascimento'):
        self.nome = nome
        self.sobrenome = sobrenome
        self.email = email
        self.bairro = bairro
        self.nascimento = nascimento


class Cartao:
    def __init__(self, idcartao=int, idusu=int, creditos=float, tipocartao=str, emissao=datetime):
        self.idcartao = idcartao
        self.idusu = idusu
        self.creditos = creditos
        self.tipocartao = ['comum', 'estudante', 'vale-transporte', 'idoso']
        self.emissao = emissao


class Onibus:
    def __init__(self, numplaca=int, numlinha=int, modelobus=str, anofabrica=datetime, idmotorista=int):
        self.numplaca = numplaca
        self.numlinha = numlinha
        self.modelobus = modelobus
        self.anofabrica = anofabrica
        self.idmotorista = idmotorista


class Motorista:
    def __init__(self, idmotorista=int, numcnh=int, nome=str, sobrenome=str, nascimento=datetime):
        self.idmotorista = idmotorista
        self.numcnh = numcnh
        self.nome = nome
        self.sobrenome = sobrenome
        self.nascimento = nascimento


