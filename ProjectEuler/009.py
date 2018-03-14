"""A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 3**2 + 4**2 = 5**2.
             9    + 16   = 25

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc."""


def is_pyth_trip(a,b,c):
    if a**2 + b**2 == c**2:
        return True
    else:
        return False

"""a = p * q
b = (p2 - q2)/2
c = (p2 + q2)/2"""

def get_pyth_trips():
    for p in range(999,0,-2):
        for q in range(999,0,-2):
            a = p * q
            b = int((p ** 2 - q **2 ) / 2)
            c = int((p ** 2 + q **2 ) / 2)

            if is_pyth_trip(a,b,c) and a+b+c == 1000:
                return a*b*c

print(get_pyth_trips())
print("done")
