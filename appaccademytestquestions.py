# We're going to implement a cipher called the Folding Cipher. Why? Because it
# folds the alphabet in half and uses the adjacent letter.
#
# For example,
# a <=> z
# b <=> y
# c <=> x
# ...
# m <=> n
#
# Hint: Think about zipping some things together.


tab = str.maketrans("abcdefghijklmnopqrstuvwxyz","zyxwvutsrqponmlkjihgfedcba")
#print("hello my old friend".translate(tab))

# Write a method that returns the factors of a number

number = "33"

def factor(n):
    factors = []
    for i in range (n):
        if i == 0:
            pass
        elif n % i == 0:
            factors.append(i)
    factors.append(n)
    return factors


# Jumble sort will take a string and return a string with the letters ordered
# according to the order of an alphabet array that will be handed to the method.
# If no alphabet array is provided, it should default to alphabetical order.

abc = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v",
    "w","x","y","z"]

def jumble_sort(string,alphabet=abc):
    for i in string:
            new_string= zip(string,alphabet)
    return new_string

alphabet_string = "abcdefghijklmnopqrstuvwxyz"
lyrics = "uptown funk gonna give it to ya"
cypher = "zyxwvutsrqponmlkjihgfedcba"
cypher_list=[]
for l in cypher:
    cypher_list.append(l)
print(cypher_list)
cy_list = ['z', 'y', 'x', 'w', 'v', 'u', 't', 's', 'r', 'q', 'p', 'o', 'n', 'm', 'l', 'k', 'j', 'i', 'h', 'g', 'f', 'e', 'd', 'c', 'b', 'a']





# Write an array method that returns `true` if the array has duplicated
# values and `false` if it does not

my_string = "hello from the other side"
my_list = [1,2,5,3,9,3,8,32]

def has_duplicate(list):
    sorted_array = sorted(list)
    length = len(sorted_array)
    result = 0


    for i in range(1,(length+1)):
        print(i)
        if sorted_array[i] == sorted_array[i-1]:
            return True

        else:
            result = False
    return result
print(has_duplicate(my_list))

# Determine if a string is symmetrical. 'racecar' and
# 'too hot to hoot' are examples of symmetrical strings.
# You are NOT permitted to use Array#reverse,
# Array#reverse!, String#reverse, or String#reverse!
"""
string2 = "raCecar"

reverse = ""
for i in string:
    reverse = i + reverse
if string2.lower() == reverse.lower():
    print(string, "is a palindrome")
else:
    print(string, "is not a palindrome")
"""
