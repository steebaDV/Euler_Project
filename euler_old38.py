def pan(n):
    number_of_digits = -1
    counter = 1
    numbers = set()
    string = ''
    while (number_of_digits < 9) or (number_of_digits == -1):
        for number in str(n * counter):
            if number == '0':
                return False
            numbers.add(int(number))
        if number_of_digits == -1:
            number_of_digits = 0
        number_of_digits += len(str(n * counter))
        string += str(n * counter)
        counter += 1
    if number_of_digits > 9:
        return False
    elif len(numbers) == 9:
        pans.append(string)
        return True
    else:
        return False


pans = []
for i in range(1, 10 ** 5):
    if pan(i):
        print(i,pans[-1])
print(max(pans))
