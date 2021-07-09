def disc(k):
    di = 1 + 24 * k
    sqrt = di ** 0.5
    if (di > 0) and int(sqrt) == sqrt:
        if (1 + sqrt) / 6 == int((1 + sqrt) / 6):
            return (1 + sqrt) / 6
        else:
            return 0
    else:
        return 0


amount = 10 ** 4
numbers = [n * (3 * n - 1) // 2 for n in range(1, 2* amount)]
d = 5482661
for i in range(3, amount - 1):
    print(i)
    i_n = numbers[i]
    for j in range(i + 1, amount - 2):
        j_n = numbers[j]
        minimal = abs(i_n - j_n)
        if minimal < d:
            max_ = disc(i_n + j_n)
            min_ = disc(minimal)
            if (max_ == 0) or (min_ == 0):
                continue
            if (max_ == int(max_)) and (min_ == int(min_)):
                d = minimal
                print(i_n, j_n)
                print(minimal, i_n + j_n)
                print(i)
                print()
print(d)
