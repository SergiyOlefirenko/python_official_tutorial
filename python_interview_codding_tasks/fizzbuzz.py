# result = ''
# for n in range(100):
#     if n % 3 == 0 and n % 5 == 0:
#         result = 'FizzBuzz'
#     elif n % 5 == 0:
#         result = 'Buzz'
#     elif n % 3 == 0:
#         result = 'Fizz'
#     else:
#         result = n
#     print(result)


mappings = {3: 'Fizz', 5: 'Buzz'}
result = []
for i in range(20):
    s = ''
    for key in mappings:
        if i % key == 0:
            s += mappings[key]
    if not s:
        s = str(i)
    result.append(s)
print('\n'.join(result))