class Usuario:
    def __init__(self, nome=str, sobrenome=str, email=str, bairro=str, nascimento='nascimento'):
        self.nome = nome
        self.sobrenome = sobrenome
        self.email = email
        self.bairro = bairro
        self.nascimento = nascimento

    def get_nome(self): #getter
        return self.nome

    def get_sobrenome(self):
        return self.sobrenome

    def get_email(self):
        return self.email

    def get_bairro(self):
        return self.bairro

    def get_nascimento(self):
        return self.nascimento

    def set_nome(self, novo_nome):#setter
        self.nome = novo_nome

    def set_sobrenome(self, novo_sobrenome):
        self.sobrenome = novo_sobrenome

    def set_email(self, novo_email):
        self.email = novo_email

    def set_bairro(self, novo_bairro):
        self.bairro = novo_bairro

    def set_nascimento(self, nova_data):
        self.nascimento = nova_data
class Cartao:
    def __init__(self, idcartao=int, idusu=int, creditos=float, tipocartao=str, emissao='emissao'):
        self.idcartao = idcartao
        self.idusu = idusu
        self.creditos = creditos
        self.tipocartao = ['comum', 'estudante', 'vale-transporte', 'idoso']
        self.emissao = emissao


class Onibus:
    def __init__(self, numplaca=int, numlinha=int, modelobus=str, anofabrica='ano_fabrica'):
        self.numplaca = numplaca
        self.numlinha = numlinha
        self.modelobus = modelobus
        self.anofabrica = anofabrica



class Motorista:
    def __init__(self, numcnh=int, nome=str, sobrenome=str, nascimento='nascimento'):
        self.numcnh = numcnh
        self.nome = nome
        self.sobrenome = sobrenome
        self.nascimento = nascimento

