def triangle_number_2(n: int):
    for linha in range(1, n + 1):
        for coluna in range(1, linha + 1):
            print(coluna, end='   ')
        print('')


triangle_number_2(5)
