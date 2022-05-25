import numpy as np


bus = np.arange(40).reshape(8, 5)
bus[1:8, 0] = 1
bus[1:8, 1] = 1
bus[1:8, 3] = 1
bus[1:8, 4] = 1
bus[0] = 0
bus[1:8, 2] = 0
bus[0][0] = 2


def menu_inicial():
    print("_" * 30, """
    Bem vindo ao Sistema de Compras do PoccoBus!

    [1] Comprar passagem:
    [2] Verificar polronas disponíveis:
    [3] Sair""")

    try:
        m = int(input('Digite a opçao desejada: '))

        if m == 1:
            rodar_programa()

        elif m == 2:
            print(bus)
            print("""As poltronas marcadas com 1 estao disponíveis,
                  as poltronas marcadas com 0 nao sao permitidas viajar,
                  as poltronas marcadas com 3 estao ocupadas por outros passageiros,
                  a poltrona número 2 é do motorista.""")
            menu_inicial()

        elif m == 3:
            mensagem_sair()
            salvar_poltronas()
            exit()

        else:
            print('Escolha uma opçao válida!')
            menu_inicial()

    except ValueError:
        print('Escolha uma opçao válida!')
        menu_inicial()


def reservar_assento(x, y):

    try:
        if bus[x][y] == 2:
            print('Tá doido? Esse é o lugar do motorista!'
                  'Escolha outro: ')

        elif bus[x][y] == 0:
            print('Viajar no corredor é muito perigoso, por favor escolha um assento que esteja livre!')

        elif bus[x][y] == 1:
            bus[x][y] = 3
            print('Seu lugar foi reservado com sucesso!')
            print('O lugar que você escolheu foi marcado como OCUPADO.')

        elif 'OCUPADO' in bus[x][y]:
            print('Assento ocupado, escolha outro!')

    except IndexError:
        print('Os valores que você digitou nao representam uma célula da matriz, '
              'por favor tente novamente!')

    continuar_comprando()


def escolher_linha():
    global x

    try:

        x = int(input('Para selecionar seu assento você deve primeiro digitar a linha da célula que deseja reservar,'
                      'considere a primeira linha como 0 e a última como 7 ou digite 9 para sair: '))
        if 0 <= x <= 7:
            pass

        elif x == 9:
            mensagem_sair()
            salvar_poltronas()
            exit()

        else:
            print('Seu valor foi inválido, insira um número entre 0 e 7 '
                  'referente á linha na qual se encontra o lugar que você deseja ocupar na matriz, '
                  'ou digite 9 para sair')
            escolher_linha()

    except ValueError:
        print('Você digitou caracteres inválidos, insira um número entre 0 e 7 para reservar ou '
              'digite 9 para sair.')
        escolher_linha()


def escolher_coluna():
    global y

    try:

        y = int(input('Agora escolhe a coluna onde se encontra o assento que deseja ocupar,'
                      'considere a primeira linha como 0 e a última como 4 ou digite 9 para sair: '))

        if 0 <= y <= 4:
            pass

        elif y == 9:
            mensagem_sair()
            salvar_poltronas()
            exit()

        else:
            print('Seu valor foi inválido, insira um número entre 0 e 4'
                  'referente á coluna na qual se encontra o lugar que você deseja ocupar na matriz')
            escolher_coluna()
    except ValueError:
        print('Você digitou caracteres inválidos, insira um número entre 0 e 4 para reservar ou 9 para sair')
        escolher_coluna()


def mensagem_sair():
    print('Esperamos ver você em breve, até logo')


def rodar_programa():
    escolher_linha()
    escolher_coluna()
    reservar_assento(x, y)


def continuar_comprando():
    nova_compra = int(input('Deseja continuar comprando ? '
                            'Digite 1 para continuar ou 2 para encerrar.'))

    try:
        if nova_compra == 1:
            salvar_poltronas()
            menu_inicial()

        elif nova_compra == 2:
            mensagem_sair()
            salvar_poltronas()

        else:
            print('Você digitou um valor inválido.')
            continuar_comprando()

    except ValueError:
        continuar_comprando()


def salvar_poltronas():
    with open('Ônibus atualizado', 'w+') as busao:
        for linha in bus:
            busao.write(str(linha) + '\n')


menu_inicial()
