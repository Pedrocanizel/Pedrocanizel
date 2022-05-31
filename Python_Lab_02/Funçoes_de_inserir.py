def cadastrar_usuario():
    new_user = Usuario()
    nome = str(input('Digite seu nome >>> '))
    sobrenome = str(input('Digite seu sobrenome >>> '))
    email = str(input('Digite seu email >>> '))
    bairro = str(input('Digite seu bairro >>> '))
    data_nascimento = str(input('Digite sua data de nascimrnto [YYYY-MM-DD] >>> '))
    new_user.set_usuario(f'{nome}, {sobrenome}, {email}, {bairro}, {data_nascimento}')
    print('Usuário cadastrado com sucesso, você será redirecionado para o '
          'menu inicial para decidir o que deseja realizar em seguida.')
    menu_inicial()

def cadastrar_cartao():
    new_card = Cartao()
    id_cartao = int(input('Digite o ID do seu cartao >>> '))
    id_usuario = int(input('Digite seu ID de usuário >>> '))
    creditos = float(input('Digite quantos créditos você deseja inserir >>> '))
    perg_tipo_cartao = int(input("""Qual é o tipo do seu cartao?
    
    [1] Comum
    [2] Estudante
    [3] Vale-transporte
    [4] Idoso
    
    >>> """))
    if perg_tipo_cartao == 1:
        tipo_cartao = 'comum'
    elif perg_tipo_cartao == 2:
        tipo_cartao = 'estudante'
    elif perg_tipo_cartao == 3:
        tipo_cartao = 'vale-transporte'
    elif perg_tipo_cartao == 4:
        tipo_cartao = 'idoso'
    else:
        print('Você digitou um valor inválido, preste mais atençao')
        cadastrar_cartao()
    data_emissao = str(input('Digite a data de emissao do seu cartao [YYYY-MM-DD] >>> '))
    new_card.set_cartao(f'{id_cartao}, {id_usuario}, {creditos}, {tipo_cartao}, {data_emissao}')
    print('Cartao cadastrado com sucesso, você será redirecionado para o '
          'menu inicial para decidir o que deseja realizar em seguida.')
    menu_inicial()

def cadastrar_onibus():
    new_bus = Onibus()
    num_placa = int(input('Digite o número da placa >>> '))
    num_linha = int(input('Digite o número da linha >>> '))
    modelo_bus = str(input('Digite o modelo do ônibus >>> '))
    ano_fabrica = str(input('Digite a data de fabricacao [YYYY-MM-DD] >>> '))
    id_motorista = int(input('Digite seu número de identificaçao >>> '))
    new_bus.set_onibus(f'{num_placa}, {num_linha}, {modelo_bus}, {ano_fabrica}, {id_motorista}')
    print('Ônibus cadastrado com sucesso, você será redirecionado para o '
          'menu inicial para decidir o que deseja realizar em seguida.')
    menu_inicial()

def cadastrar_motorista():
    new_driver = Motorista()
    cnh = int(input('Digite sua CNH >>> '))
    nome = str(input('Digite seu nome >>> '))
    sobrenome = str(input('Digite seu sobrenome >>> '))
    data_nascimento = str(input('Digite sua data de nascimrnto [YYYY-MM-DD] >>> '))
    new_driver.set_motorista(f'{cnh}, {nome}, {sobrenome}, {data_nascimento}')
    print('Motorista cadastrado com sucesso, você será redirecionado para o '
          'menu inicial para decidir o que deseja realizar em seguida.')
    menu_inicial()
