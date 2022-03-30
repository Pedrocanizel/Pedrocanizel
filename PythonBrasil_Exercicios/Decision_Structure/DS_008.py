p1 = 'Rice'
p2 = 'Beans'
p3 = 'Pasta'

n1_price = float(input(f"What's the {p1} price?"))
n2_price = float(input(f"What's the {p2} price?"))
n3_price = float(input(f"What's the {p3} price?"))

if n1_price < n2_price and n1_price < n3_price:
    print(f'The cheapest is {p1}, its cost is {n1_price}')

elif n2_price < n1_price and n2_price < n3_price:
    print(f'The cheapest is {p2}, its cost is {n2_price}')

elif n3_price < n1_price and n3_price < n2_price:
    print(f'The cheapest is {p3}, its cost is {n3_price}')

elif n1_price < n2_price and n1_price == n3_price:
    print(f'The cheapest are {p1} and {p3}')

elif n2_price < n1_price and n2_price == n3_price:
    print(f'The cheapest are {p2} and {p3}')

elif n1_price < n3_price and n1_price == n2_price:
    print(f'The cheapest are {p1} and {p2}')

elif n1_price == n2_price == n3_price:
    print('They have the same price')
