amount_last_10 = 0
for i in range(1, 1001):
    amount_last_10 += i ** i
    string = str(amount_last_10)
    length = len(string)
    if length > 10:
        difference = length - 10
        amount_last_10 = int(string[difference:])
print(amount_last_10)