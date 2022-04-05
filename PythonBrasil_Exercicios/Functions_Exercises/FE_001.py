def triangle_number(n: int):
    for i in range(1, n + 1):
        for _ in range(i):
            print(i, end='   ')
        print('')


triangle_number(5)
