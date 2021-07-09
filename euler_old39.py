counter = 0
i = 0
d = 1
amount = 0
while counter != 7:
    i += 1
    number = str(i)
    amount += len(number)
    if amount >= 10 ** counter:
        d *= int(number[-(amount - 10 ** counter + 1)])
        counter += 1
print(d)

