# A tuple consists of a number of values separated by commas
t = 12345, 54321, 'hello!'
print(t[0])
print(t)

# tuples can be nested
u = t, (1, 2, 3, 4, 5)
print(u)

# tunle are immutable
# t[0] = 8888 ==> TypeError: 'tuple' object does not support item assignment

# tuples can contain mutable objects
v = ([1, 2, 3], [3, 2, 1])
print(v)
# mutable objects can be changed
v[0].append(4)
print(v)

'''
Tuples are immutable, and usually contain a heterogeneous sequence of elements that are accessed via unpacking 
(see later in this section) or indexing (or even by attribute in the case of namedtuples). 
Lists are mutable, and their elements are usually homogeneous and are accessed by iterating over the list.
'''


empty = ()
singleton = 'hello',
print(len(empty))
print(len(singleton))
print(singleton)

x, y, z = t
print(x, y, z)
