eph = float(input('How much do you earn per hour?'))
hwm = float(input('How much hours do you work by month?'))
gs = eph * hwm
inss_tax = gs * 0.11
sin_tax = gs * 0.05
ns = gs - sin_tax - inss_tax

print(f'Your gross salary is {gs}')
print(f'You Inss tax os {inss_tax}')
print(f'Your sindicate tax is {sin_tax}')
print(f'Your net salary is {ns}')
