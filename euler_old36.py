def numeral_system(n, p=2):
    counter = n
    number = ''
    while counter >= p:
        number = str(counter % p) + number
        counter //= p
    number = str(counter) + number
    return number


def palindrom(n):
    if n == n[::-1]:
        return True
    else:
        return False


print(sum([i for i in range(10 ** 6) if
           palindrom(str(i)) == True and palindrom(
               numeral_system(i)) == True]))