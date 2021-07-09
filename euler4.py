"""
    A palindromic number reads the same both ways.
    The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
    Find the largest palindrome made from the product of two 3-digit numbers.
"""

palindrome = 0
for num1 in range(100, 1000):
    for num2 in range(100, 1000):
        prod = num1 * num2
        prod_str = str(prod)
        if prod > palindrome and prod_str == prod_str[::-1]:
            palindrome = prod

print(palindrome)
