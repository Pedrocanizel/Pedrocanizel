class Pessoa:
    def __init__(self, nome=None, idade=35):
        self.idade = idade
        self.nome = nome

if __name__ == '__main__':
    p = Pessoa()
    print(p.nome)
    print(p.idade)
