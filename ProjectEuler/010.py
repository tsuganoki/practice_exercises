"""The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million."""



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
"""

def get_n_primes(n):
    primeslist = []
    p = 2
    while len(primeslist) < n:
        p = get_next_prime(p)
        primeslist.append(p)
        p +=1
    return primeslist

def get_primes_below(n):
    primeslist = []
    p = 2
    while p < n:
        p = get_next_prime(p)
        if p < n:
            primeslist.append(p)
        p +=1
    return primeslist
"""
def sum_primes_below(n):
    total = 0
    p = 2
    while p < n:
        p = get_next_prime(p)
        if p < n:
            total += p
        p += 1
    return total
#142913828922
#print(get_primes_below(2e6))
print(sum_primes_below(2e6))

print("Done")
