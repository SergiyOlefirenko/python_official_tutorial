num = 50

for n in range(1, num):
    if n > 1:
        for i in range(2, n):
            if n % i == 0:
                break
        else:
            print(n)