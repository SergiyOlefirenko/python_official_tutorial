basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banna'}
print(basket) # show that duplicates have been removed

print('orange' in basket) # fast membership testing
print('crabgrass' in basket)

# Demonstrate set operations on unique letters from two words
a = set('abracadabra')
print(a)
b = set('alacazam')
print(b)

print(f'letters in a but not in b {a - b}')
print(f'letters in a or b or both {a | b}')
print(f'letters in both a and b {a & b}')
print(f'letter in a or b but not in both {a ^ b}')


# Similarly to list comprehensions, set comprehensions are also supported:
a = {x for x in 'abracadabra' if x not in 'abc'}
print(a)
# print(a[0]) ==> TypeError: 'set' object is not subscriptable