def firstn(n):
    num = 0
    nums = []
    while num < n:
        nums.append(num)
        num += 1
    return nums


"""   1 # a generator that yields items instead of returning a list
   2 def firstn(n):
   3     num = 0
   4     while num < n:
   5         yield num
   6         num += 1
   7
   8 sum_of_first_n = sum(firstn(1000000))"""
from math import sqrt
#from itertools import ifilter

def first_n(n):
    num = 0
    while num < n:
        yield num
        num +=1

def is_prime(num):
    for i in range(2,(int(sqrt(num))+1)):
        if num % i == 0:
            return False
    return True

def get_primes():
    num = 2
    while True:
        if is_prime(num):
            yield num
        num +=1

def ends_in_twentyone(num):
    if str(num)[-2:] == "21":
        return True


# so for a generator that goes ad infinitum, you can't use or min or max, because it won't
# become a valid target for a min,max function till it finishes running
# in order to filter for the first result that passes a test, you need to use the following
# syntax, and it must be in python

# print(filter(ends_in_twentyone,get_primes()).__next__())
# print(filter(ends_in_twentyone,get_primes())[0])


"""
for i in get_primes():
    if str(i)[-2:] == "21":
        print("success: ", i)
        break
"""

def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False


f= first_n(12)
"""
for i in f:
    print(is_even(i))
"""
"""for i in range(4):
    print(list(first_n(i)))
"""
