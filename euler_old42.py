def shift(massive):
    summa = 0
    length = len(massive)
    max_value = max(massive)
    flag_1 = True
    while flag_1:
        flag_2 = True
        number = ''
        i = 2
        while i != length + 1 and massive[-i] > massive[-i + 1]:
            i += 1
        point = -i
        if i == length + 1:
            flag_1 = False
            break
        value = max_value
        key = massive.index(value)
        for digit in range(point + 1, 0):
            if (massive[digit] > massive[point]) and (massive[digit] < value):
                value = massive[digit]
                key = digit
        massive[key], massive[point] = massive[point], massive[key]
        massive = massive[:point + 1] + sorted(massive[point + 1:])
        for i in massive:
            number += str(i)
        for i in range(7):
            if int(number[1 + i:4 + i]) % prime[i] != 0:
                flag_2 = False
                break
        if flag_2:
            summa += int(number)
            print(number)
    return summa


prime = [2, 3, 5, 7, 11, 13, 17]
digit = [0, 9, 8, 7, 6, 5, 4, 3, 2, 1]
wow = shift(digit)
print(wow)
