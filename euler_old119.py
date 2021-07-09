import math


def nod(a, b):
    while b!= 0:
        a,b = b,a % b
    return a


a = 0
b = []
for i in range(1,100):
    for j in range(2,10):
        p = i**j
        summa = sum([int(k) for k in str(p)])
        if i == summa and p > 9:
            b.append(p)
b.sort()
print(b)
print(b[29])

