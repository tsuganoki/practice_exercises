#Your next challenge shall be to code FizzBuzz, a common intro-question to screen out job applicants.

#Write a function that prints out all the integers from 1 to 100.

#However, for each number evenly divisible by three, the number shall be replaced with the string "fizz", and for each number divisible by 5, the number shall be replaced by the string "buzz".

#For numbers divisible by both, print "fizz buzz"

def fizzbuzz():
    for i in range(1:101):
        if i % 3 == 0 and i % 5 !=0:
            print("fizz")
        elif i % 5 == 0 and i % 3 != 0:
            print("buzz")
        elif i % 3 == 0 and i % 5 == 0:
            print("fizz buzz")
        else:
            print(i)

fizzbuzz()
