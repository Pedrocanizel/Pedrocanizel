vowel = ['a', 'e', 'i', 'o', 'u']
consonant = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n',
             'p', 'q', 'r', 's', 't', 'v', 'x', 'z']

let = input('Enter a letter:').lower()

if let in vowel:
    print(f'The letter {let} is a vowel')

elif let in consonant:
    print(f'The letter {let} is a consonant')

else:
    print('Invalid input')
