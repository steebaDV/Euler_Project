"""
    By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
    What is the 10 001st prime number?
"""

from funcs import sieveOfEratosthenes
import numpy as np

n = 10001
primes = sieveOfEratosthenes(130000)
print(primes[primes > 0][n - 1])