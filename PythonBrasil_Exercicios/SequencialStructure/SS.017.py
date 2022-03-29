import math

area_m2 = 16
area_10 = area_m2 * 1.1
paint_lt = area_10 / 6
can_lt = 18
can_num = math.ceil(paint_lt / can_lt)
can18_value = can_num * 80
gal_lt = 3.6
gal_num = math.ceil(paint_lt / gal_lt)
gal_value = gal_num * 25

print(f'Você deverá usar {can_num} latas de 18 litros, no valor de R${can18_value}')
print(f'Você deverá usar {gal_num} latas de 18 litros, no valor de R${gal_value}')
