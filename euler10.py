"""
    The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
    Find the sum of all the primes below two million.
"""

from funcs import sieveOfEratosthenes

primes = sieveOfEratosthenes(2 * 10 ** 6 - 1)
print(sum(primes))
