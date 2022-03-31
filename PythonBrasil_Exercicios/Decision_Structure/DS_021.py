with_amo = 299

note_100 = note_50 = note_10 = note_5 = note_1 = 0

note_100, with_amo = divmod(with_amo, 100)

note_50, with_amo = divmod(with_amo, 50)

note_10, with_amo = divmod(with_amo, 10)

note_5, note_1 = divmod(with_amo, 5)

if note_100 > 0:
    print(f'{note_100} 100s notes')

if note_50 > 0:
    print(f'{note_50} 50s notes')

if note_10 > 0:
    print(f'{note_10} 10s notes')

if note_5 > 0:
    print(f'{note_5} 5s notes')

if note_1 > 0:
    print(f'{note_1} 1s notes')
