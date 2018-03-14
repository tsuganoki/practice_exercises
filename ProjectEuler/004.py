"""A palindromic number reads the same both ways. The largest
palindrome made from the product of two 2-digit numbers is 9009 = 91 * 99.

Find the largest palindrome made from the product of two 3-digit numbers.

998001
10000
"""
import itertools
import functools

def is_pal(n):
    fwd = list(str(n))
    back = list(reversed(fwd))
    return fwd == back

def products():
    for i in range(999,900,-1):
        for j in range(i,900,-1):

            yield (i*j)


ans = max(filter(is_pal,products()))
print(ans)
