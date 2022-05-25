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
