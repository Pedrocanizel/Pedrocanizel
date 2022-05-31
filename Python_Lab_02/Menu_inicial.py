def menu_inicial():
    print(""" Bem Vindo ao sistema de cadastro de dados da PoccoBus,
 selecione qual açao você deseja realizar: 
    
    [1] Realizar cadastro;
    
    [2] Verificar tabelas;
    
    [3] Sair.""")


    opçao = int(input(''))

    if opçao == 1:

    elif opçao == 2:

    elif opçao == 3:
        mensagem_sair()
        exit()

    else:
        print('Você digitou uma opçao inválida')
        menu_inicial()



def mensagem_sair():
    print('Esperamos ver você em breve, até logo')

menu_inicial()
