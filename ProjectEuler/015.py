"""Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20×20 grid?"""


paths = []
from math import factorial



def run_it(n,r):
    ans = (factorial(n))/ (factorial(r) * (factorial(n-r)))
    return ans

print(run_it(40,20))
