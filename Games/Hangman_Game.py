word = 'DevPro'.upper()

print('Hangman game, Discover the word: ')

print('The word is: ', end='')
for letter in word:
    print(f'_ ', end='')

setletter_word = set(word)
setenter_letter = set()
errors = 0

while not setletter_word.issubset(setenter_letter) and errors < 7:
    print()
    print()
    enter_letter = input('Enter a letter').upper()
    setenter_letter.add(enter_letter)
    if enter_letter in setletter_word:
        print('The word is: ', end='')
        for letter in word:
            if letter in setenter_letter:
                print(f'{letter} ', end='')
            else:
                print(f'_ ', end='')
    else:
        errors += 1
        print(f'Erro {errors} from 6. Try again!')

    print()
    print('Entered letters: ', setenter_letter)

if errors < 7:
    print('You Win')
else:
    print('You loose')
