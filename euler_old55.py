lychrel_numbers = 0
for i in range(1, 10 ** 4):
    counter = 1
    s = str(i)
    flag = True
    while counter != 50:
        s = str(int(s) + int(s[::-1]))
        if s == s[::-1]:
            flag = False
            break
        counter += 1
    if flag:
        lychrel_numbers += 1
        print(i)
print(lychrel_numbers)
