"""2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?"""


"""upper = 1
numlist = [20,19,18,17,16,15,14,13,12,11]
for i in numlist:
    upper *= i
"""
upper =  670442572800

def has_factor(num,factor):
    if num % factor == 0:
        return True
    else:
        return False


def has_factors(num,lis):
    for i in lis:
        if has_factor(num, i) == False:
            return False
    return True

my_list = [100,85]
#print(has_factors(30,my_list))

def get_n(a,b,interval,lis):
    for i in range(a,b,interval):
        if has_factors(i,lis) == True:
            return i

numlist = [19,18,17,16,15,14,13,12,11]


print(get_n(2520,upper,20,numlist))
