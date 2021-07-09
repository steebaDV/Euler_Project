factor = [1, 1]
counter = 0
for i in range(2, 101):
    factor.append(factor[-1] * i)
for n in range(23, 101):
    r = 1
    while factor[n]//(factor[n - r] * factor[r]) <= 10**6:
        r += 1
    while factor[n]//(factor[n - r] * factor[r]) > 10**6:
        print('n =', n, 'r =', r)
        r += 1
        counter += 1
print(counter)