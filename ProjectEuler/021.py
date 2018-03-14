"""Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000."""

from math import sqrt

def get_divs_sum(num):
    divs = [1,]
    for i in range(2,int(sqrt(num)+1)):
        if num % i == 0:
            if int(sqrt(num)) == i:
                divs.append(i)
            else:
                divs.append(i)
                divs.append(int(num/i))
    return sum(divs)

def get_amicables(num):
    divs_sums = []
    amicables = []
    amicables_sum = 0
    for i in range(num):
        divs_sums.append([i,get_divs_sum(i)])
        if get_divs_sum(i) == i:
            pass
        elif [get_divs_sum(i),i] in divs_sums:
            print([get_divs_sum(i),i])
            #amicables.append([get_divs_sum(i),i])
            amicables_sum += i + get_divs_sum(i)


    return sorted(amicables),amicables_sum

print(get_amicables(10000))
#print(get_divs_sum(220))
