from sieve_of_eratosthenes import sieve_2 as sv

pr = sv(10 ** 4)
prime = [i for i in pr if (i != 0) and (i > 1000)]
length_prime = len(prime)
for i in range(length_prime - 1):
    numbers = [prime[i]]
    digits_i = [0] * 10
    for k in str(prime[i]):
        digits_i[int(k)] += 1
    for j in range(i + 1, length_prime):
        digits_j = [0] * 10
        for k in str(prime[j]):
            digits_j[int(k)] += 1
        if digits_i == digits_j:
            numbers.append(prime[j])
    if len(numbers) > 2:
        length_numbers = len(numbers)
        differences = []
        for j in range(length_numbers - 2):
            for k in range(j+1,length_numbers-1):
                for l in range(k+1,length_numbers):
                    if numbers[l] - numbers[k] == numbers[k] - numbers[j]:
                        print(str(numbers[j]) + str(numbers[k]) + str(numbers[l]))
