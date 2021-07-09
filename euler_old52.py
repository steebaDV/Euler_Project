i = 0
while True:
    i += 1
    digits = set([int(j) for j in str(i)])
    flag = True
    for j in range(2, 8):
        if digits != set([int(k) for k in str(i * j)]):
            flag = False
            break
    if flag:
        print(i)
        break
