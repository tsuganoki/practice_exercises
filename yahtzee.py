from random import randint
import pdb
#import numpy as np

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

# rolls all 5 dice and returns a dictionary
def roll_all():
    rolls = {}
    dice = "ABCDE"
    for i in range(5):
        rolls[(dice[i])] = randint(1,6)
    return rolls

# takes a user input and outputs a list containing only the letters ABCDE
def convert_to_list(us_sel):
    us_sel_list = []
    for i in us_sel:
        if ord(i.lower()) > 96 and ord(i.lower()) <102:
            us_sel_list.append(i.upper())
    return us_sel_list

#function which sanitizes any input and returns a lowercase string
def sanit(input):
    input = input.lower()
    output = ""
    for i in input:
        if ord(i) > 96 and ord(i) <102:
            output = output + i
    return i



# rerolls specified dice from a list of user inputs
def reroll(l,rolls):
    for i in l:
        rolls[i] = randint(1,6)
    return rolls



# function for displaying the dice results to the user
def display_roll(rolls):
    for key in sorted(rolls.iterkeys()):
        print "%s: %s" % (key, rolls[key])
    print(" ")


# This function gets the user's reroll choice and returns a list with [choice, round]
def reroll_choice():
    #pdb.set_trace()

    rerollyn = raw_input("Reroll? (Y / N) ")
    print(" ")
    if sanit(rerollyn[0]) == "n":
        #if the user inputs a string starting with "n", no re-roll happens
        return True

    elif sanit(rerollyn[0]) == "y":
        #if the user inputs a string starting with "y"
        return False
    else:
        #if the user does a keyboard smash, it will start over
        print("I didn't understand that input. Please Try again.")
        return reroll_choice()



"""def get_reroll_choice(rolls):
    #this section asks the user for a reroll choice
    output = []
    rerollyn = ""
    rerollyn = raw_input("Reroll? (Y / N) ")
    print(" ")

    if sanit(rerollyn[0]) == "n":
        #if the user inputs a string starting with "n", no re-roll happens
        return True

    elif sanit(rerollyn[0]) == "y":
        #if the user inputs a string starting with "y" it will ask for which dice to reroll
        user_selection = raw_input("Reroll? (A, B, C, D, E?) ")
        print(" ")
        print("Rerolling....")

        reroll(convert_to_list(user_selection),rolls)

        print("Your new rolls are: ")
        display_roll(rolls)
        return False


    else:
        #if the user does a keyboard smash, it will start over
        print("I didn't understand that input. Please Try again.")
        get_reroll_choice(rolls)
"""

def select_dice(rolls):
    user_selection = raw_input("Enter which die or dice to reroll: A, B, C, D, E ")
    print(" ")

    user_selection_list = convert_to_list(user_selection)
    if len(user_selection_list) < 1:
        print("Please type a letter or letters (not case sensitive)")
        select_dice(rolls)
    print("Rerolling....")
    rolls = reroll(user_selection_list,rolls)
    return rolls

def stringify_key_value_cat(key,value):
    return value + "(" +  str(key) + ")"

def display_categories(categories):
    string_list_up = []
    string_list_low = []

    for key in filter(lambda key: categories[key][0],categories):
        if key < 7:
            string_list_up.append(stringify_key_value_cat(key,categories[key][1]))
        else:
            string_list_low.append(stringify_key_value_cat(key,categories[key][1]))

    print("Remaining options: ")
    if string_list_up == []:
        print("Upper: None")
    else:
        print("Upper: "+ ", ".join(string_list_up))
    if string_list_low == []:
        print("Lower: None.")
    else:
        print("Lower: " + ", ".join(string_list_low))


def select_category_fun(categories):

    display_categories(categories)
    cat_selection = raw_input("Select a category to score this round: ")
    try:
        cat_selection = int(cat_selection)
    except:
        print("Response not understood. Please try again.\n")
        return select_category_fun(categories)
    if cat_selection > 0 and cat_selection < 14:
        if categories[cat_selection][0] == False:
            print("That category is no longer available. Please try again. ")
            return select_category_fun(categories)
        else:
            return int(cat_selection)
    else:
        print("Response not understood. Please try again.\n")
        return select_category_fun(categories)


#This function takes in a user selection and a set of rolls, and returns a list of points for that roll
def score_fun(rolls_dict,cat_selection,game_score):

    score_upper = 0
    score_lower = 0
    yahtzee = 0
    is_yahtzee = False
    score_list = [0,0,0]

    #Changes rolls to a simple ordered list
    rolls = []
    for key in rolls_dict:
        rolls.append(rolls_dict[key])
    rolls.sort()

    rolls_string = ""
    for i in rolls:
        rolls_string += str(i)
    #checks if yahtzee
    if all(x==rolls[0] for x in rolls):
        is_yahtzee = True

    if cat_selection < 7:
        for i in rolls:
            if i == cat_selection:
                score_upper += i

    elif cat_selection == 7: #three of a Kind
        rolls1 = rolls[:3]
        rolls2 = rolls[1:4]
        rolls3 = rolls[2:]
        if all(x==rolls1[0] for x in rolls1) or all(x==rolls2[0] for x in rolls2) or all(x==rolls3[0] for x in rolls3):
            score_lower = 17
    elif cat_selection == 8:#four of a kind
        if rolls[0] == rolls [3] or rolls[1] == rolls[4]:
            score_lower = 24

    elif cat_selection == 9: #Full House (two of a kind and three of a kind)
        rolls1=rolls[:3]
        rolls2 = rolls[3:]

        rolls3 = rolls[:2]
        rolls4 = rolls[2:]

        if all(x==rolls1[0] for x in rolls1) and all(x==rolls2[0] for x in rolls2):
            score_lower = 25
        elif all(x==rolls3[0] for x in rolls3) and all(x==rolls4[0] for x in rolls4):
            score_lower = 25

    elif cat_selection == 10: #large Straight (5)
        if rolls == [1,2,3,4,5] or rolls == [2,3,4,5,6]:
            score_lower = 40
            print("i am a potato")

    elif cat_selection == 11:#Small Straight (4)
        if "1234" in rolls_string or "2345" in rolls_string or "3456" in rolls_string:
            score_lower = 30

    elif cat_selection == 12: #Chance(sum of all dice)
        for i in rolls:
            score_lower += i

    elif cat_selection == 13: #yahtzee
        if is_yahtzee == True:
            yahtzee  = 1
            score_lower = 50

    if is_yahtzee == True and game_score[2] > 0:
        score_lower +=100
    score_list[0] = score_upper
    score_list[1] = score_lower
    score_list[2] = yahtzee
    return score_list


# Function for Displaying Score:
def display_score(score_list):
    u_bonus = ""
    y_bonus = ""
    if score_list[0] > 63:
        u_bonus = "Upper Section Bonus: +35 Points for hitting 63!"
    if score_list[2] == 0:
        yahtzee_score = 0
    elif score_list[2] > 1:
        y_bonus = "Yahtzee Bonus: +100 points!"


    total = score_list[0] + score_list[1]

    print("Score Upper: %s %s" % (score_list[0],u_bonus))
    print("Score Lower: %s" % (score_list[1]))
    print("Yahtzees: %s %s" % (score_list[2],y_bonus))
    print("Score Total: %s" % (total))
    print(" ")

def add_round_score(score,points):
    sum = []
    for i,k in zip(score,points):
        sum.append(i+k)
    return sum

# Function for running a single round
def new_round(categories,game_score):
    round_output = {}
    round_score = [0,0,0]

    #this section gives the initial roll
    rolls = roll_all()
    print("Your initial rolls are: ")
    display_roll(rolls)

    #sets the roll count for the round to 2 remaining
    round_roll_count = 2

    #asks the user for a reroll up to two times
    print("You have %s rolls remaining." % (round_roll_count))
    while round_roll_count >0:
        reroll_choice_var = reroll_choice()
        print(reroll_choice_var)
        if reroll_choice_var == False:

            rolls = select_dice(rolls)
            round_roll_count += -1
            print("Your new rolls are: ")
            display_roll(rolls)
        else:
            print("Keeping rolls. ")
            print(" ")
            round_roll_count += -3


    cat_selection = select_category_fun(categories)

    #this line sets the selected category to False, so it can't be used again
    categories[cat_selection][0]= False


    #round is scored here
    #this function takes in your rolls, and your selection, and returns a list of round points
    round_score = score_fun(rolls,cat_selection,game_score)

    print(" ")
    print("Your score for this round was: %s" %(round_score[0]+round_score[1]))
    #display_score(round_score)


    #round info is added to a dictionary
    round_output["round_score"] = round_score
    round_output["categories"] = categories



    # returns a dictionary with all the round info in it
    return round_output


def play_yahtzee():
    round_count = 1
    upper_bonus = False
    yahtzee_bonus = 0
    game_score = [0,0,0]
    number_of_rounds = 13
    game = {}


    #This is how scoring categories are tracked
    categories = {1:[True,"Aces"],2:[True,"Twos"],3:[True,"Threes"],4:[True,"Fours"],5:[True,"Fives"],6:[True,"Sixes"],
    7:[True,"Three of a Kind",7],8:[True,"Four of a Kind",8],9:[True,"Full House",9],10:[True,"Small Straight",10],
    11:[True,"Large Straight"],12:[True,"Chance"],13:[True,"Yahtzee"]}


# this is the section where the game happens
    while round_count < (number_of_rounds+1):
        #this section lists the round number
        print("Round "+ str(round_count)),
        print(" ")

        #runs 1 round and stores the rolls, score, and categories in round_output, also adds it to a dictionary
        round_output = new_round(categories,game_score)
        categories = round_output["categories"]

        #stores the round in a master game dictionary
        game[round_count] = round_output

        #add round_pounds to game_points
        game_score = add_round_score(game_score,round_output["round_score"])

        #checks for Upper Bonus and Yahtzee Bonus
        if game_score[0] > 63 and upper_bonus == False:
            game_score[0] += 35
            upper_bonus = True
        if game_score[2] > 1:
            game_score[1] += 100
        display_score(game_score)
        if round_count < number_of_rounds:
            pause = raw_input("Hit any key to start next round...")

        #uh?
        #print("upper score from round output:", round_output["score_upper"])

        #incriments the round number
        round_count +=1

    restart = raw_input("Good Game! You scored a total of %s Points! Play again?" % (game_score[0] + game_score[1]))
    if sanit(restart)[0] == "y":
        play_yahtzee()



if __name__ == '__main__':
    play_yahtzee()
    pass


categories = {1:[True,"Aces",1],2:[True,"Twos",2],3:[True,"Threes",3],4:[True,"Fours",4],5:[True,"Fives",5],6:[True,"Sixes",6],
    7:[True,"Three of a Kind",7],8:[True,"Four of a Kind",8],9:[True,"Full House",9],10:[True,"Small Straight",10],
    11:[True,"Large Straight",11],12:[True,"Chance",12],13:[True,"Yahtzee",13]}
"""
game_score = [0,0,0]


rolls = {
    'A': 1,
    'B': 1,
    'C': 1,
    'D': 1,
    'E': 1,
    }

#score_fun(rolls,cat_selection,game_score):
#n = int(raw_input(" : "))
round_score = score_fun(rolls,12,game_score)

display_score(round_score)
"""
