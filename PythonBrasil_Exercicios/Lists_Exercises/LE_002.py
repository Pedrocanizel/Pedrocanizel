ll = []

for n in range(10):
    num = float(input('Enter a number'))
    ll.append(num)

print(ll[::-1])
ll.reverse()
print(ll)
