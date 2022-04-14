llist = []


def mb_transform(byte_size: str):
    return int(byte_size) / (2**10) ** 2


with open('users.txt', 'r') as file:
    for line in file:
        line = line.strip()
        user = line[:15]
        disc_size = mb_transform(line[16:])
        llist.append((user, disc_size))


top_page = '''ACME Inc.               Uso do espaço em disco pelos usuários
------------------------------------------------------------------------
Nr.  Usuário        Espaço utilizado     % do uso
'''

with open('report.txt', 'w') as file:
    total_size = sum(size for _, size in llist)
    media = total_size / len(llist)
    file.writelines(top_page)
    for index, data in enumerate(llist, start=1):
        user, disc_size = data
        file.writelines(
            f'{index:<4} {user} {disc_size:9.2f} MB          '
            f'{disc_size/total_size:>6.2%}\n'
        )

    file.writelines('\n')
    file.writelines(f'Used size: {total_size:.2f} MB\n')
    file.writelines(f'Media is: {media:.2f} MB ')
