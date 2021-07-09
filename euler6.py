"""
    Find the difference between
    the sum of the squares of the first one hundred natural numbers and the square of the sum
"""
sum_of_the_squares = 0
square_of_the_sum = 0

for num in range(1,101):
    sum_of_the_squares += num * num
    square_of_the_sum += num

square_of_the_sum *= square_of_the_sum

print(square_of_the_sum - sum_of_the_squares)