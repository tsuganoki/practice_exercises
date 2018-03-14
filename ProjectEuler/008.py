"""
The four adjacent digits in the 1000-digit number that have the greatest product are 9 × 9 × 8 × 9 = 5832.

Find the thirteen adjacent digits in the 1000-digit number that have the greatest product. What is the value of this product?

"""
num = 731671765313306249192251196744265747423553491949349698352031277450632623957831801698480186947885184385861560789112949495459501737958331952853208805511125406987471585238630507156932909632952274430435576689664895044524452316173185640309871112172238311362229893423380308135336276614282806444486645238749303589072962904915604407723907138105158593079608667017242712188399879790879227492190169972088809377665727333001053367881220235421809751254540594752243525849077116705560136048395864467063244157221553975369781797784617406495514929086256932197846862248283972241375657056057490261407972968652414535100478216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450

num_list = list(str(num))


#takes a long digit, num, and a number of places, n, and returns a list of all n digit sets
def get_list(num,n):
    lis = list(str(num))
    num_list = []
    while len(lis) >= n:
        temp = lis[(n*-1):]
        item = ""
        for i in temp:
            item +=i
        num_list.append(int(item))
        lis.pop()


    return num_list


# takes a n digit number, and multiplies each one
def multiply_digits(n):
    lis = str(n)
    product = 1
    for i in lis:
        product *= int(i)
    return product

print(list(map(multiply_digits,get_list(1234,2))))


note = "Please ignore everything below here: "
note2 = " ================================== "

#print(multiply_digits(23))
prac_num = 123456789

#print(get_list(prac_num,3))
"""print(get_list(234,2))
print(multiply_digits(34))

print(get_list(num,13))"""

max_product = 0

def get_max():
    for i in get_list(num,13):
        if multiply_digits(i) > max_product:
            print(multiply_digits(i))
            max_product = multiply_digits(i)
    return max_product

#print(max_product)
print(get_list(1234,2))
items = [1, 2, 3, 4, 5]
squared = map(lambda x: x**2, items)
#print(squared)
