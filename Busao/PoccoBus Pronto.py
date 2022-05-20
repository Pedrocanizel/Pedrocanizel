bus = [['MOTORISTA', 'CORREDOR', 'CORREDOR', 'CORREDOR', 'CORREDOR'],
       ['LIVRE', '    LIVRE', '   CORREDOR', 'LIVRE', '   LIVRE'],
       ['LIVRE', '    OCUPADO', ' CORREDOR', 'LIVRE', '   LIVRE'],
       ['LIVRE', '    LIVRE', '   CORREDOR', 'LIVRE', '   LIVRE'],
       ['LIVRE', '    LIVRE', '   CORREDOR', 'LIVRE', '   LIVRE'],
       ['LIVRE', '    LIVRE', '   CORREDOR', 'LIVRE', '   LIVRE'],
       ['LIVRE', '    LIVRE', '   CORREDOR', 'LIVRE', '   LIVRE'],
       ['LIVRE', '    LIVRE', '   CORREDOR', 'LIVRE', '   LIVRE']]


def reservar_assento(x, y):

    try:
        if 'MOTORISTA' in bus[x][y]:
            print('Esse é o lugar do motorista!')

        elif 'CORREDOR' in bus[x][y]:
            print('Viajar no corredor é muito perigoso, por favor escolha um assento que esteja livre!')

        elif 'LIVRE' in bus[x][y]:
            bus[x][y] = 'OCUPADO'
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
        print('A MAtriz abaixo representa o ônibus que você vai viajar,'
              'escolha um local seguro e faça boa viagem!''\n')
        for fila in bus:
            print(fila)

        x = int(input('Para selecionar seu assento você deve primeiro digitar a linha da célula que deseja reservar,'
                      'considere a primeira linha como 0 e a última como 7 ou digite 9 para sair:'))
        if 0 <= x <= 7:
            pass

        elif x == 9:
            mensagem_sair()
            salvar_poltronas()
            exit()

        else:
            print('Seu número foi menor do que 0 ou maior do que 7, insira um número entre 0 e 7 '
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

        y = int(input('Agora escolha a coluna onde se localiza a célula que deseja reservar ou digite 9 para sair:'))

        if 0 <= y <= 4:
            pass

        elif y == 9:
            mensagem_sair()
            salvar_poltronas()
            exit()

        else:
            print('Seu número foi menor do que 0 ou maior do que 4, insira um número entre 0 e 4'
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
            rodar_programa()
            salvar_poltronas()

        elif nova_compra == 2:
            mensagem_sair()
            salvar_poltronas()

    except ValueError:
        continuar_comprando()


def salvar_poltronas():
    with open('Ônibus atualizado', 'w') as busao:
        for linha in bus:
            busao.write(str(linha) + '\n')


rodar_programa()
