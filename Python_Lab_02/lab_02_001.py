import datetime
import pyodbc

dados_conexao = (
    "Driver={MySQL ODBC 8.0 ANSI Driver};"
    "Server=DESKTOP-3776R5G;"
    "Database=db_lab_02;"
    "username=pedro;"
    "password=8158;"
)

conexao = pyodbc.connect(dados_conexao)
print("conexao bem sucedida")


class Usuario:
    def __init__(self, idusu=int, nome=str, sobrenome=str, email=str, bairro=str, nascimento=datetime):
        self.idusu = idusu
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


