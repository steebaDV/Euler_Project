"""
    215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

    What is the sum of the digits of the number 21000?
"""

import numpy as np
digits = np.array([0] * 301 + [1])

for n in range(1, 1001):
    digits *= 2
    index = -1
    for index in range(-1, -302, -1):
        digits[index - 1] += digits[index] // 10
        digits[index] %= 10
        index -= 1

print(sum(digits))
