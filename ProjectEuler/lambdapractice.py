
from functools import reduce


def multiply_by_five(num):
    return num * 5

lis = [1,2,3,4,5,6,7,8,9,10]

# this applies the function *5 to each n in iterable "lis"
new_lis = list(map(lambda num: num * 5,lis))

#this multiplies the next entry by the previous result
product = reduce((lambda x, y: x * y), [1, 2, 3, 4])

#print(product)


def factorial(n):
    num = 1
    for i in range (1,(n+1)):
        num *=i
        yield num

list_of_factorials = list(map(multiply_by_five,factorial(3)))
print(list_of_factorials)


for i in factorial(5):
    print(i)


"""
def fact(n):

    return result"""

#print(fact(3))
