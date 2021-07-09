"""
    Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
    If d(a) = b and d(b) = a, where a ≠ b,
    then a and b are an amicable pair and each of a and b are called amicable numbers.

    For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284.
    The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

    Evaluate the sum of all the amicable numbers under 10000.
"""

from funcs import get_divisors

sum_of_friendly_numbers = 0
for num in range(2, 10000):
    sum_of_divisors = sum(get_divisors(num)) - num
    if sum_of_divisors != num and sum(get_divisors(sum_of_divisors)) - sum_of_divisors == num:
        sum_of_friendly_numbers += num


print(sum_of_friendly_numbers)
