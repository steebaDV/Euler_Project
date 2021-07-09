from sieve_of_eratosthenes import sieve_2 as sv


def pr_d(n):  # prime decomposition
    s = 0
    number = n
    for pr_number in prime:
        if number == 1:
            break
        if pr_number == 0:
            continue
        else:
            flag = False
            while number % pr_number == 0:
                number //= pr_number
                flag = True
            if flag:
                s += 1
    return s


n = 4
prime = sv(10 ** 6)
i = 1
counter = 0
while counter != n:
    i += 1
    if pr_d(i) == n:
        counter += 1
    else:
        counter = 0
print(i - n + 1)
