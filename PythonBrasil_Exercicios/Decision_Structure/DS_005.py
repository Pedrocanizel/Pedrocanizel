n1 = float(input('Enter a note: '))
n2 = float(input('Enter another note '))
media = (n1 + n2) / 2

if 7 <= media < 10:
    print('Accredited')

elif media < 7:
    print('Disapproved')

elif media == 10:
    print('Approved with honor')

