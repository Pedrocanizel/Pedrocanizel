number = 20
hund_str = doz_str = uni_str = ''
part_num = 0

hund_int, number = divmod(number, 100)

if hund_int == 1:
    hund_str = '1 hundred'
    part_num += 1

elif hund_int > 1:
    hund_str = f'{hund_int} hundreds'
    part_num += 1

doz_int, number = divmod(number, 10)

if doz_int == 1:
    doz_str = '1 dozen'
    part_num += 1

elif doz_int > 1:
    doz_str = f'{doz_int} dozens'
    part_num += 1

if number == 1:
    uni_str = '1 unit'
    part_num += 1

elif number > 1:
    uni_str = f'{number} units'
    part_num += 1

if part_num == 0:
    print('Number 0 dosent have hundreds, dozens and units')

elif part_num == 1:
    print(hund_str + doz_str + uni_str)

elif part_num == 3:
    print(f'{hund_str}, {doz_str} e {uni_str}')

elif part_num == 2:
    if hund_str != '':
        sec_part = doz_str + uni_str
        print(f'{hund_str} and {sec_part}')

    else:
        print(f'{doz_str} and {uni_str}')

print(hund_str + doz_str + uni_str)
