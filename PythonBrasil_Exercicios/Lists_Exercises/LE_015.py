notes = []
while True:
    entry = input('Enter a number')
    if entry == '-1':
        break
    notes.append(float(entry))

lenght = len(notes)

print(f'The lenght of the list was {lenght}.')
print(' '.join([str(note) for note in notes]))

notes.reverse()

for note in notes:
    print(note)

summ = sum(notes)
media = summ / lenght

print(f'The sum of the notes is {summ}')
print(f'The media is {media}')
print(' '.join([str(note) for note in notes if note > media]))
print(' '.join([str(note) for note in notes if note < 7]))
print('Finished')
