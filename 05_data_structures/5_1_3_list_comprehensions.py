'''
List comprehensions provide a concise way to create lists.
'''

# creating list of squares using for loop
squares = []
for x in range(10):
    squares.append(x**2)
print(squares)

# creating list with map and lambda functions
squares = list(map(lambda x: x**2, range(10)))
print(squares)

# using list comprehension
squares = [x**2 for x in range(10)]
print(squares)

# listcomp combines the elements of two lists if they are not equal:
listcomp = [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
print(listcomp)
# the same with for loops
combs = []
for x in [1,2,3]:
    for y in [3,1,4]:
        if x != y:
            combs.append((x, y))
print(combs)


vec = [-4, -2, 0, 2, 4]
# create a new list with the values doubled
doubled_vec = [x*2 for x in vec]
print(doubled_vec)
# filter the list to exclude negative numbers
no_negative_num = [x for x in vec if x >= 0]
print(no_negative_num)
# call method on each elemnt
freshfruit = ['  banana', '  loganberry', 'passion fruit  ']
fruits = [fruit.strip() for fruit in freshfruit]
print(fruits)
# create a list of 2-tuples like (number, square)
two_tuple_list = [(x, x**2) for x in range(6)]
print(two_tuple_list)
# the tuple must be parenthesized, otherwise an error is raised
# [x, x**2 for x in range(6)]

# flatten a list using a listcomp with two 'for'
vec = [[1,2,3], [4,5,6],[7,8,9]]
flatten_list = [num for elem in vec for num in elem]
print(f'{vec} ==> {flatten_list}')

# list comprehensions can contain complex expressions and nested functions
from math import pi
nested_fun_listcomp = [str(round(pi, i)) for i in range(1,6)]
print(nested_fun_listcomp)