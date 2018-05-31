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

def diceroller():

    cont = True
    while cont== True:
        dicestring = sanitize(input("Dice to roll: "))

        num = ""
        die = ""
        print(dicestring)
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
        print("Final roll total: " + str(total))
        print(" ")
        reroll = sanitize(input("Reroll? Y/N " ))
        if reroll == "n" or reroll == "exit":
            cont = False
            print("Thanks for rolling")


diceroller()
