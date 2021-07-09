from sieve_of_eratosthenes import sieve_2 as sv


def omg(number_of_digits):
    number_size = 10 ** (number_of_digits - 1)
    for n in range(1, number_of_digits):
        massive = wow(number_of_digits, n)
        amount_of_digits = 10 ** (number_of_digits - n)
        for digit in range(amount_of_digits):
            digits = [i for i in str(digit)]
            for j in massive:
                numbers = []
                counter = 0
                for k in range(10):
                    digits_copy = digits[:]
                    number = ''
                    for i in j:
                        digits_copy.insert(i, str(k))
                    for l in digits_copy:
                        number += l
                    number = int(number)
                    if (number > number_size) and prime[number] != 0:
                        numbers.append(number)
                        counter += 1
                        if counter == 8:
                            print(numbers)
                            return min(numbers)
    return 0


def wow(digits, n):
    a = list(range(n))
    b = []
    b.append(a[:])
    point = -1
    now = point
    while True:
        flag = True
        for i in range(-n, 0):
            if a[i] == digits + i:
                point = i - 1
                flag = False
                break
        if point == -(n + 1):
            break
        if flag:
            point = -1
        a[point] += 1
        if now != point:
            now = point
            for i in range(point + 1, 0):
                a[i] = a[point] + i - point
        b.append(a[:])
    return b


prime = sv(10 ** 7)
for n in range(2, 11):
    x = omg(n)
    if x != 0:
        print(x)
