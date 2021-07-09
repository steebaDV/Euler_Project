from sieve_of_eratosthenes import sieve_1 as sv

prime = sv(2* 10**8)
print('wow')
number = 1
counter = 2
amount = 1
pr_numbers = 0
for j in range(2):
    for i in range(4):
        number += counter
        if prime[number] != 0:
            pr_numbers += 1
    amount += 4
    counter += 2
    print(number)
    print(amount//4 * 2 + 1)
    print(pr_numbers / amount)
    print()
    if pr_numbers / amount < 0.1:
        break
print(amount//4 * 2 + 1)