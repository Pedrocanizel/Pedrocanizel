class CirculoPerfeito:
    def __init__(self):
        self.cor = 'Azul'
        self.circunferencia = 4
        self.material = 'Papel'

    def mostra_cor(self):
        return self.cor

    def troca_cor(self, cor):
        self.cor = cor


circulo_primeiro = CirculoPerfeito()

print(circulo_primeiro.cor, circulo_primeiro.circunferencia, circulo_primeiro.material)
