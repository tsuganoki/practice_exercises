# Dice Roller v2
from random import randint

#dice = input("Dice to roll: ")
info_msg = "\nWelcome to Tilia's Dice Roller.\n\nType a number followed by the letter \"d\" followed by another number to roll some dice. The first number is the quantity of dice. The second number is the type of die or the number of sides on each die.\nType \"q\" to exit.\nType "r" to repeat the previous roll.\nType \"help\" to repeat this prompt. \n"

error_msg = "\nThat's not a valid roll. Please try again.\n"

prev_roll = None

def err():
    print(error_msg)

def sanitize(string):
    """Takes a str as input, removes weird chars, and outputs the 
    string in lower case

    """
    string = string.lower()
    newstring = ""
    for i in string:
        if i.isalnum():
            newstring += i
    return newstring

def roll_em(num,die):
    """Takes a quantity "num" and a die-type "die", rolls 'em, and 
    prints each roll and the total and returns the total"""
    total = 0
    while num > 0:
        roll = randint(1,die)
        total += roll
        print(roll)
        num -=1
    return total

def display_total(total):
    print("\nFinal roll total: {}".format(total))

def crit_check(dicestring,total):
    if dicestring =="1d20":
        if total > 19:
            print("\n!!! Critical threat !!! \n")
            reroll = randint(1,20)
            print("Original roll: {0}    Reroll: {1}\n ".format(total,reroll))
            
        elif total < 2:
            print("!!! Critical threat !!! \n") 
            reroll = randint(1,20)
            print("Original Roll: {0}    Reroll: {1}\n ".format(total,reroll))



def diceroller():
    """diceroller has no parameters; runs until the user exits

    while diceroller is running, it will continually loop, starting 
    out with asking for the user to input a "roll." The input must 
    start with a number, end with a number, and only contain the letter
    "d" in between. It is not case sensitive, and the user may put 
    spaces or not between them. 
    If the input is not recognized, an error message will appear, and 
    it wil send the user back to the original prompt. 
    If the user types "help" it will display a helpful message.
    If the user types "q" (not case sensitive), it will end the program.
    If the user types "r" (not case sensitive), it will reuse the previous roll.
    
    """
    prev_roll = None
    while True:
        dicestring = sanitize(input("\nDice to roll: "))

        num = ""
        die = ""
        #print(dicestring)
        if dicestring == "q":
            print("Thanks for rolling!\n")
            break
        elif dicestring == "r":
            if prev_roll == None:
                print("No Previous rolls available.")
                continue
            else:
                dicestring = prev_roll
        elif dicestring == "help":
            print(info_msg)
            continue
        elif len(dicestring) < 3 or "d" not in dicestring:
            err()
            continue
        for i in range(len(dicestring)):

            if dicestring[i] == "d":
                num = dicestring[:i]
                die = dicestring[(i+1):]
        if not num.isdecimal() or not die.isdecimal():
            err()
            continue
        

        num = int(num)
        die = int(die)

        if num < 1 or die < 2 : # num must be at least 1, and die must be at least 2
            err()
            continue

        print("\nRolling {0} d{1}...".format(num,die))

        total = roll_em(num,die)
        if num > 1:
            display_total(total)
        crit_check(dicestring,total)
        prev_roll = dicestring

        

        
        #reroll = sanitize(input("Reroll? Y/N " ))
        #if reroll == "n" or reroll == "exit":
        #    cont = False
            

print(info_msg)
diceroller()
