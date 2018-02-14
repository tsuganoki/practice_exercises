"""By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?"""

from math import sqrt
from itertools import count

def is_prime(n):
    for i in range(2,int(sqrt(n)+1)):
        if n % i == 0:
            return False
    return True


def get_next_prime(n):
    prime = False
    while prime == False:
        if is_prime(n):
            prime = True
            return n
        else:
            n += 1


def get_primes(n):
    primeslist = []
    p = 2
    while len(primeslist) < n:
        p = get_next_prime(p)
        primeslist.append(p)
        p +=1
    return primeslist


#ans = (get_primes(10001))[-1]

print(get_primes(10))
