from sieve_of_eratosthenes import sieve_1 as sv

prime_numbers = sv(10 ** 6)
cycle_numbers = []
for i in prime_numbers:
    if i == 0:
        continue
    else:
        print(i)
    length = len(str(i))
    flag = True
    number = i
    numbers = [i]
    for j in range(1, length):
        x = number % 10
        number //= 10
        number += x * (10 ** (length - 1))
        if number not in prime_numbers:
            flag = False
    if flag:
        for j in numbers:
            if j not in cycle_numbers:
                cycle_numbers.append(j)
print(len(cycle_numbers))

