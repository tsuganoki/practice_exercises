from random import randint
import pdb
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



#round_roll_count = 0

def dieroll():
    return randint(1,6)


# rolls all 5 dice
def roll_all():
    rolls = []
    for i in range(5):
        rolls.append(dieroll())
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
def reroll(l,rolls):
    for i in l:
        index = ord(i)-97
        rolls[index] = dieroll()
    return rolls



# function for displaying the dice results to the user
def display_roll(rolls):
    n = 65
    for i in rolls:
        string = chr(n)+ ": " + str(i)
        print(string)
        n +=1
    print(" ")

# This function gets the user's reroll choice



def get_choice(rolls):
    #this section asks the user for a reroll choice
    rerollyn = ""
    rerollyn = raw_input("Reroll? (Y / N) ")
    print(" ")

    if sanit(rerollyn[0]) == "n":
        #if the user inputs a string starting with "n", no re-roll happens
        print("Keeping Rolls")

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
        get_choice(rolls)


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

    if string_list_up == []:
        print("Upper: None")
    else:
        print("Upper: "+ ", ".join(string_list_up))
    if string_list_low == []:
        print("Lower: None.")
    else:
        print("Lower: " + ", ".join(string_list_low))

#This function displays remaining score categories and returns a valid user selection
def select_category_fun(rolls,categories):

    print("Please select a scoring Category from the remaining options: ")

    """cat_list_upper = ""
    cat_list_lower = ""

    cat_list_upper_sel = ""
    cat_list_lower_sel = ""

    cat_keys = categories.keys()



    for key in categories:
        #pdb.set_trace()

        if key < 7:

            if categories[key][0] == True:
            #print("this is the boolian: ", str(categories[key][0]))
            #print("this is the category: ")
            #print(categories[key][1])

                cat_string_upper = categories[key][1]

                #cat_list_upper = cat_list_upper + ", " + cat_string_upper
                cat_list_upper = cat_list_upper + cat_string_upper + "(" +  str(key) + "), "

            #print(cat_list)
        elif key >6 :
            if categories[key][0] == True:


                cat_string_lower = categories[key][1]

                #cat_list_lower = cat_list_lower + cat_string_lower +"(" +  str(categories[key][2]) + ")"
                cat_list_lower =
    cat_list_upper = cat_list_upper[:-2]
    cat_list_lower = cat_list_lower[:-2]
    print("Upper: "+ str(cat_list_upper))
    print("Lower: "+ str(cat_list_lower))"""
    #print("In the upper section there are six categories. The score in each of these boxes is determined by adding the total number of dice matching that box.")

    display_categories(categories)

    cat_selection = int(raw_input("Select a category to score this round: "))
    if cat_selection > 0 and  cat_selection < 14:
        if categories[cat_selection][0] == False:
            print("That category is no longer available. Please try again. ")
            select_category_fun(categories,rolls)
        else:
            return int(cat_selection)
    else:
        print("I didn't understand that response. Please try again.")
        select_category_fun(categories,rolls)


#This function takes in a user selection and a set of rolls, and returns a list of score criteria
def score_fun(rolls,cat_selection):
    score_list = [0,0,False]
    score_upper = 0
    score_lower = 0
    yahtzee = False
    if cat_selection < 7:
        for i in rolls:
            if i == cat_selection:
                score_upper +=cat_selection
    score_list[0] = score_upper
    score_list[1] = score_lower
    score_list[2] = yahtzee





    return score_list

# Function for running a single round
def new_round(categories):
    round_done = False
    rolls = []

    round_output = {}


    #this section gives the initial roll
    rolls = roll_all()
    print("Your initial rolls are: ")
    display_roll(rolls)


    #sets the roll count for the round to 1
    round_roll_count = 1

    #asks the user for a reroll up to two times
    print("You have "+ str(3- round_roll_count) +" rolls remaining.")

    round_done = get_choice(rolls)

    #print("this is directly after the first get chouce",round_done)

    if round_done == False:
        round_roll_count += 1
        print("You have "+ str(3- round_roll_count) +" rolls remaining.")
        get_choice(rolls)

    cat_selection = select_category_fun(rolls,categories)
    categories[cat_selection][0]= False
    print(cat_selection)


    score_list = score_fun(rolls,cat_selection)
    score_upper = score_list[0]
    score_lower = score_list[1]
    yahtzee = score_list[2]

    print(score_list)

    round_output["rolls"] = rolls
    round_output["score_upper"] = score_upper
    round_output["score_lower"] = score_lower
    if yahtzee == True:
        round_output["yahtzee"] = 1
    else:
        round_output["yahtzee"] = 0






    #round is scored here
    print(" ")



    #input_upper_lower()

    #round ends
    print("thank you.")

    # I forgot what this does
    return round_output


def play_yahtzee():
    round_count = 1
    score = 0
    score_upper = 0
    score_lower = 0
    yahtzee = 0
    score_list = [score_upper,score_lower,yahtzee]
    game = {}

    #This is how scoring categories are tracked

    categories = {1:[True,"Aces",1],2:[True,"Twos",2],3:[True,"Threes",3],4:[True,"Fours",4],5:[True,"Fives",5],6:[True,"Sixes",6],
    7:[True,"Three of a Kind",7],8:[True,"Four of a Kind",8],9:[True,"Full House",9],10:[True,"Small Straight",10],
    11:[True,"Large Straight",11],12:[True,"Chance",12],13:[True,"Yahtzee",13]}


    while round_count < 3:
        #this section lists the round number
        print("Round "+ str(round_count)),
        print(" ")

        #runs 1 round
        round_output = new_round(categories)


        print("upper score from round output:", round_output["score_upper"])

        #stores the round in a master game dictionary
        game[round_count] = round_output

        print("this is the value I'm trying to add to score_upper: ", round_output["score_upper"])
        score_upper += round_output["score_upper"]
        print("this is score_upper after attempting to add the round total", score_upper)
        score_lower += round_output["score_lower"]
        if round_output["yahtzee"] == True:
            yahtzee += 1

        score_list = [score_upper,score_lower,yahtzee]
        print("score at the end of this round is: ",score_list)


        round_count +=1



    restart = raw_input("Good Game! Play again?")
    if sanit(restart)[0] == "y":
        play_yahtzee()



if __name__ == '__main__':
    play_yahtzee()

#new_round(categories)
