"""2 ** 15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2 ** 1000?"""

def run_it(power):
    string = str(2 ** power)
    result = 0
    for i in string:
        result += (int(i))

    return result

print(run_it(1000))
