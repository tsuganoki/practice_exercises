# Dice Roller v2
from random import randint

#dice = input("Dice to roll: ")

def sanitize(string):
    string = string.lower()
    newstring = ""
    for i in string:
        if i.isalnum():
            newstring += i
    return newstring

def diceroller(dicestring):
    num = ""
    die = ""
    for i in range(len(dicestring)):

        if dicestring[i] == "d":
            num = dicestring[:i]
            die = dicestring[(i+1):]

    print(" ")
    print("Rolling " + num + " D " + die + "...")
    num = int(num)
    die = int(die)
    total = 0
    while num > 0:
        roll = randint(1,die)
        total += roll
        print(roll)
        num -=1

    print(" ")
    return "Final roll total: " + str(total)


print(diceroller(sanitize(input("Dice to roll: "))))
