"""The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?"""

##code a function "primes" which accepts an argument, "num", and returns the first num prime numbers in order
from math import sqrt
from math import floor

def is_prime(n):
    for i in range(2,int(sqrt(n)+1)):
        if n % i == 0:
            return False
    return True

def primes():
    n = 1
    while True:
        if is_prime(n):
            yield n
        n += 1

num = 600851475143

num2 = 13195

def get_big_prime_factor(num):
    root = int(sqrt(num))
    for i in range(root,0,-1):
        if is_prime(i):
            if num % i == 0:
                return i

print(get_big_prime_factor(num))
