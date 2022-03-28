import math

sw = float(input('Whats is the size of the wall?'))
tl = sw / 3
ql = tl / 18
ctc = 80

print(f'You will need {math.ceil(ql)} paint cans and it will cost {math.ceil(ql) * ctc}')
