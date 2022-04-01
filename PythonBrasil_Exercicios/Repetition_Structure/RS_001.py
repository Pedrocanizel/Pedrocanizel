while True:
    try:
        number = int(input('Enter a number between 0 and 10: '))
    except ValueError:
        print('Must be an int.')
    else:
        if 0 <= number <= 10:
            print(f'Input number is : {number}')
            break
        else:
            print('The number must be between 0 and 10')
