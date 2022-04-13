name = input('Enter a name: ').upper()

inv_by_letters = ''.join(reversed(name))
inv_by_words = ' '.join(reversed(name.split()))

print(name)
print(f'Name inverted by letters: {inv_by_letters}')
print(f'Name inverted by word: {inv_by_words}')
