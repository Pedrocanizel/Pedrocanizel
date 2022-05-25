lugares_que_nao_podem = [7, 12, 17, 22, 27, 32, 37]
matriz = []


def criar_matriz():
    linha = []
    lugares = 1
    for s in range(5):
        linha.append(lugares)
        lugares += 1
    for i in range(8):
        matriz.append(linha)

    return matriz

a = criar_matriz()
print(a)
#def colorir_matriz(matriz):
#    for lugar in matriz:
#        if lugar == 0:






#a = criar_matriz()
#print(a)

#for num in matriz:
#    if 0 in num:
#        print('x')
#    print(num)

#print(lista)
#print(matriz)
