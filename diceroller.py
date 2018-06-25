# Dice Roller v2
from random import randint

#dice = input("Dice to roll: ")
info_msg = "\nWelcome to Tilia's Dice Roller.\n\nType a number followed by the letter \"d\" followed by another number to roll some dice.\nType \"q\" to exit.\nType \"help\" to repeat this prompt. \n"
error_msg = "\nThat's not a valid dice roll. Please try again.\n"
def sanitize(string):
    string = string.lower()
    newstring = ""
    for i in string:
        if i.isalnum():
            newstring += i
    return newstring

def diceroller():

    
    while True:
        dicestring = sanitize(input("Dice to roll: "))

        num = ""
        die = ""
        print(dicestring)
        if dicestring == "q":
            break
        elif dicestring == "help":
            print(info_msg)
            continue
        elif len(dicestring) < 3 or "d" not in dicestring:
            print(error_msg)
            continue
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

print(info_msg)
diceroller()
