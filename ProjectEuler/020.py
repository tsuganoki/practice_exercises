"""n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!"""

def get_factorial(num):
    num_fact = 1
    while num >1:
        num_fact*=num
        num -=1
    return num_fact

def sum_digits(num):
    total = 0
    for i in str(num):
        total += int(i)
    return total

print(sum_digits(get_factorial(100)))
