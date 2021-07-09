"""
    2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
    What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""
from collections import Counter
from funcs import factorize
from functools import reduce

dict_ = Counter()
for num in range(20, 1, -1):
    counter = Counter(factorize(num))
    dict_ = dict_ | counter

print(reduce(lambda x, y: x * y, [key ** values for key, values in dict_.items()]))
