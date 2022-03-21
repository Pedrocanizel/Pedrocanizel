"""
Creating a list of numbers from inputs.

"""

n = 10
ll = []

while n > 0:
    a = int(input('Digite a number'))
    ll.append(a)
    n -= 1

print(ll)
