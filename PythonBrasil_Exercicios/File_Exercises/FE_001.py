def validar(ip: str) -> bool:
    numbers = ip.split('.')

    if len(numbers) != 4:
        return False

    for n in numbers:
        if not (0 <= int(n) <= 255):
            return False
    return True


valid_ips = []
invalid_ips = []

with open('ips.txt', 'r') as file:
    for line in file:
        ip = line.strip()
        if validar(ip):
            valid_ips.append(ip)
        else:
            invalid_ips.append(ip)
        print(line, validar(ip))

with open('ips_exit.txt', 'w') as file:
    file.writelines('[valid address:]\n')

    for ip in valid_ips:
        file.writelines(f'{ip}\n')

    file.writelines('\n')
    file.writelines('\n')
    file.writelines('[Invalid address:]\n')

    for ip in invalid_ips:
        file.writelines(f'{ip}\n')

