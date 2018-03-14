"""
The sum of the squares of the first ten natural numbers is, 385

The square of the sum of the first ten natural numbers is, 3025

Hence the difference between the sum of the squares of the first
ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one
hundred natural numbers and the square of the sum.
"""

total = 0
sum_squares = 0


for n in range(101):
    sum_squares += n**2
    total += n

squared_sum = total **2

ans = squared_sum - sum_squares

print(ans)
