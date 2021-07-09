from sieve_of_eratosthenes import sieve_2 as sv


def check(n):
    for pr_number in prime:
        if pr_number > n:
            return True
        if pr_number == 0:
            continue
        else:
            i = 1
            while True:
                expression = pr_number + 2 * i ** 2
                if expression > n:
                    break
                elif expression == n:
                    return False
                else:
                    i += 1

n = 10**5
prime = sv(n)
print('wow')
for i in range(9,n,2):
    if prime[i] != 0:
        continue
    elif check(i):
        print(i)
        break
