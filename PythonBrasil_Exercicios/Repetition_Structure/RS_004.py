pop_a = 80_000
pop_b = 200_000
gr_a = 1.03
gr_b = 1.015
years = 0

while pop_a < pop_b:
    years += 1
    pop_a = int(pop_a * gr_a)
    pop_b = int(pop_b * gr_b)

print(f'years = {years}')
print(f'pop_a = {pop_a}')
print(f'pop_b = {pop_b}')
