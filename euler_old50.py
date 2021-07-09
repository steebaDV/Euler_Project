from sieve_of_eratosthenes import sieve_2 as sv

n = 10 ** 6
prime_0 = sv(n)
prime = [i for i in prime_0 if i != 0]
length = len(prime)
amount = 0
s = 0
for i in range(length - 1):
    if prime[i] != 0:
        counter = 1
        s = 0
        while True:
            s += prime[i + counter - 1]
            if s > n:
                break
            elif prime_0[s] != 0:
                amount_now = counter
                if amount_now > amount:
                    amount = amount_now
                    wow = s
            counter += 1
print(wow)
print(amount)

