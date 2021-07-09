s = 0
for a in range(1, 100):
    for b in range(1, 100):
        c = str(a ** b)
        sum_of_digits = sum(int(i) for i in c)
        if sum_of_digits > s:
            s = sum_of_digits
print(s)