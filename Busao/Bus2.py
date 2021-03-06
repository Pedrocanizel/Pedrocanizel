bus = [['MOTORISTA', 'CORREDOR', 'CORREDOR', 'CORREDOR', 'CORREDOR'],
       ['LIVRE', 'LIVRE', 'CORREDOR', 'LIVRE', 'LIVRE'],
       ['LIVRE', 'OCUPADO', 'CORREDOR', 'LIVRE', 'LIVRE'],
       ['LIVRE', 'LIVRE', 'CORREDOR', 'LIVRE', 'LIVRE'],
       ['LIVRE', 'LIVRE', 'CORREDOR', 'LIVRE', 'LIVRE'],
       ['LIVRE', 'LIVRE', 'CORREDOR', 'LIVRE', 'LIVRE'],
       ['LIVRE', 'LIVRE', 'CORREDOR', 'LIVRE', 'LIVRE'],
       ['LIVRE', 'LIVRE', 'CORREDOR', 'LIVRE', 'LIVRE']]


def reservar_assento(x, y):

    try:
        if bus[x][y] == 'MOTORISTA':
            print('Esse é o lugar do motorista!')

        elif bus[x][y] == 'CORREDOR':
            print('Viajar no corredor é muito perigoso, por favor escolha um assento que esteja livre!')

        elif bus[x][y] == 'LIVRE':
            bus[x][y] = 'OCUPADO'
            print('Seu lugar foi reservado com sucesso!')
            print(f'O lugar que você escolheu foi marcado como {bus[x][y]}')

        elif bus[x][y] == 'OCUPADO':
            print('Assento ocupado, escolha outro!')

    except IndexError:
        print('Os valores que você digitou nao representam uma célula da matriz, '
              'por favor tente novamente!')


while True:
    try:
        x = int(input('Para selecionar seu assento você deve primeiro digitar a linha da célula que deseja reservar,'
                      'considere a primeira linha como 0 e a última como 7:'))
        if 0 <= x <= 7:
            break
        else:
            print('Seu número foi menor do que 0 ou maior do que 7, insira um número entre 0 e 7'
                  'referente á linha na qual se encontra o lugar que você deseja ocupar na matriz.')

    except ValueError:
        print('Você digitou caracteres inválidos, insira um número entre 0 e 7.')

while True:
    try:

        y = int(input('Agora digite a coluna onde se localiza a célula que deseja reservar:'))
        if 0 <= y <= 4:
            break
        else:
            print('Seu número foi menor do que 0 ou maior do que 4, insira um número entre 0 e 4'
                  'referente á coluna na qual se encontra o lugar que você deseja ocupar na matriz')

    except ValueError:
        print('Você digitou caracteres inválidos, insira um número entre 0 e 4')

reservar_assento(x, y)

with open('Ônibus atualizado', 'w') as busao:
    for linha in bus:
        busao.write(str(linha) + '\n')

