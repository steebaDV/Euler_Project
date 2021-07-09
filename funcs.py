def factorize(number):
    i = 2
    factors = []
    if number <= 1:
        raise ValueError
    while number != 1:
        while number % i == 0:
            number /= i
            factors.append(i)
        i += 1
    return factors


def sieveOfEratosthenes(limit):
    array = [0, 0] + [num for num in range(2, limit + 1)]
    for num in array[2:]:
        for i in range(num * num, limit + 1, num):
            array[i] = 0
    return array


def get_divisors(number):
    if number == 1:
        return [1]
    divisors = [1, number]
    for divisor in range(2, int(number ** 0.5)):
        if number % divisor == 0:
            divisors += [divisor, number // divisor]

    if (int(number ** 0.5)) ** 2 == number:
        divisors.append(int(number ** 0.5))
    return divisors
