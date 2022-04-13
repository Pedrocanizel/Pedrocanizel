s1 = input('Enter a string: ')
s2 = input('Enter another string: ')

size1 = len(s1)
size2 = len(s2)

print(f'"{s1}": {size1} letters')
print(f'"{s2}": {size2} letters')

size_comparison = 'diffrents'
content_comparison = 'diffrents'

if s1 == s2:
    size_comparison = 'equals'
    content_comparison = 'equals'
elif size1 == size2:
    size_comparison = 'equals'

print(f'The two strings are {size_comparison} in size')
print(f'The two strings are {content_comparison} in content')
