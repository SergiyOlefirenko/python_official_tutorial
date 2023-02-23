inpt = 745

new_num = 0

while inpt > 0:
    n = inpt % 10
    new_num = (new_num * 10) + n
    inpt = inpt // 10

print(new_num)
