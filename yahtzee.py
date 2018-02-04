from random import randint
"""import pandas as pd
import json"""


# with open("somefi")


"""
import logging
logging.basicConfig(
    filename="yahtzeelog.txt",
    level = logging.DEBUG)
logging.disable(logging.CRITICAL)
"""

roundcount = 0
rolls = []
score = 0
number_of_dice = 5
game = {}
round_done = False
#round_roll_count = 0

def diceroll():
    return randint(1,6)


# rolls all 5 dice
def roll_all():
    for i in range(number_of_dice):
        rolls.append(diceroll())
    return rolls

# I have forgotten what this function is for
def convert_to_list(us_sel):
    us_sel = us_sel.lower()
    us_sel_list = []
    for i in us_sel:
        if ord(i) > 96 and ord(i) <102:
            us_sel_list.append(i)
    return us_sel_list

#function which sanitizes user input
def sanit(input):
    input = input.lower()
    output = ""
    for i in input:
        if ord(i) > 96 and ord(i) <102:
            output = output + i
    return i



# rerolls specified dice from a list of user inputs
def reroll(l):
    for i in l:
        index = ord(i)-97
        rolls[index] = diceroll()
    return rolls



# function for displaying the dice results to the user
def display_roll():
    n = 65
    for i in rolls:
        string = chr(n)+ ": " + str(i)
        print(string)
        n +=1
    print(" ")

# This function gets the user's reroll choice



def get_choice():
    #this section asks the user for a reroll choice
    rerollyn = ""
    rerollyn = raw_input("Reroll? (Y / N) ")
    print(" ")

    if sanit(rerollyn[0]) == "n":
        #if the user inputs a string starting with "n", no re-roll happens
        print("Keeping Rolls")
        round_done = True
        print(round_done)
    elif sanit(rerollyn[0]) == "y":
        #if the user inputs a string starting with "y" it will ask for which dice to reroll
        user_selection = raw_input("Reroll? (A, B, C, D, E?) ")
        print(" ")
        print("Rerolling....")

        reroll((convert_to_list(user_selection)))

        print("Your new rolls are: ")
        display_roll()


    else:
        #if the user does a keyboard smash, it will start over
        print("I didn't understand that input. Please Try again.")
        get_choice()
def input_upper_lower():
    print("Please select a scoring Category.")
    upper_lower = raw_input("Upper(A) or Lower(B) categories? ")
    if upper_lower.lower() == "a":
        upper = True
    elif upper_lower.lower() =="b":
        lower = True
    else:
        print("I didn't understand that response. Please try again.")
        input_upper_lower()



# Function for running a single round
def new_round():
    round_done = False
    upper = False
    lower = False
    #this section lists the round number
    print("Round "),
    print(roundcount+1)
    print(" ")

    #this section gives the initial roll
    roll_all()
    print("Your initial rolls are: ")
    display_roll()
    print(" ")

    #sets the roll count for the round to 1
    round_roll_count = 1

    #asks the user for a reroll up to two times
    print("You have "+ str(3- round_roll_count) +" rolls remaining.")

    get_choice()
    if round_done == False:
        print(round_done)
        round_roll_count += 1
        print("You have "+ str(3- round_roll_count) +" rolls remaining.")
        get_choice()
    else:
        pass



    #round is scored here
    print(" ")
    #input_upper_lower()

    #round ends
    print("thank you.")

    # I forgot what this does
    game[roundcount] = rolls


def play_yahtzee():

    new_round()

    print("Good Game")

#play_yahtzee()
round_roll_count = 1
new_round()
