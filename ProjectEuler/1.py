"""Multiples of 3 and 5
Problem 1
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""

def populate_multiples(a,b):
    lis = []
    for i in range(1000):
        if i % a == 0 or i % b ==0:
            lis.append(i)
    return lis

three_five_multiples = populate_multiples(3,5)

print(three_five_multiples)
ans = sum(three_five_multiples)
print(ans)
