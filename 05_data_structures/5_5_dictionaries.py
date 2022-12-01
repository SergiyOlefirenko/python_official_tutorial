'''
It is best to think of a dictionary as a set of key: value pairs,
with the requirement that the keys are unique (within one dictionary).
'''

tel = {'jack': 4098, 'sape': 4139}
tel['guido'] = 4127
print(f'tel ==> {tel}')

del(tel['sape'])
tel['irv'] = 4127
print(f'tel ==> {tel}')

print(f'list(tel) ==> {list(tel)}')
print(f'sorted(tel) ==> {sorted(tel)}')

print('guido' in tel)
print('jack' not in tel)


# The dict() constructor builds dictionaries directly from sequences of key-value pairs:
d = dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
print(f'd ==> {d}')


# In addition, dict comprehensions can be used to create dictionaries from arbitrary key and value expressions:
d1 = {x: x**2 for x in (2, 4, 6)}
print(f'd1 ==> {d1}')

# When the keys are simple strings, it is sometimes easier to specify pairs using keyword arguments:
d2 = dict(sape=4129, guido=4127, jack=4098)
print(f'd2 ==> {d2}')
