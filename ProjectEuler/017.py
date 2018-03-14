"""If the numbers 1 to 5 are written out in words: one, two,
three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters
used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were
written out in words, how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342 (three
hundred and forty-two) contains 23 letters and 115 (one hundred
and fifteen) contains 20 letters. The use of "and" when writing
out numbers is in compliance with British usage."""

number_ones = ["","one","two","three","four","five","six","seven","eight","nine"]
number_teens = ["ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen",
"seventeen","eighteen","nineteen"]
number_tens = ["","","twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety"]
number_hundred = "hundredand"
number_hundred_solo = "hundred"
wrong_answer_list = [13140, 20845, 21114, 21115, 21124, 21151,21240]


def run_it_one(num):
    letter_ct = 0
    for i in range(num+1):
        if i <10:
            print("adding: ",number_ones[i])
            letter_ct += len(number_ones[i])
        elif i <20:
            print("adding: ",number_teens[i-10])
            letter_ct += len(number_teens[i-10])
        elif i < 100:

            print("adding: ",number_tens[int(i/10)],number_ones[i%10])

            letter_ct += len(number_tens[int(i/10)])
            letter_ct +=  len(number_ones[i%10])

        elif i <1000:
            if i % 100 == 0:
                print("adding: ",number_ones[int(i/100)],number_hundred_solo)
                letter_ct += len(number_hundred_solo) + len(number_ones[int(i/100)])
            else:

                if int(i/10) % 10 == 1:
                    print("adding: ",number_ones[int(i/100)],number_hundred,number_teens[i%10] )
                    letter_ct += len(number_ones[int(i/100)]) + len(number_hundred)
                    letter_ct +=  len(number_teens[i%10])



                else:
                    letter_ct += len(number_ones[int(i/100)]) + len(number_hundred)

                    letter_ct += len(number_tens[int(i/10)%10])
                    letter_ct +=  len(number_ones[i%10])
                    print("adding: ",number_ones[int(i/100)], number_hundred,number_tens[int(i/10)%10],number_ones[i%10])
        elif i == 1000:
            print("adding: onethousand")
            letter_ct += len("onethousand")
    return letter_ct



def run_it_two():
    letter_ct = 0
    for i in number_ones:
        #ones place
        letter_ct += len(i) * 90

        #hundreds
        letter_ct += (len(i) * 100)

    for i in number_tens:
        letter_ct += len(i) * 100

    for i in number_teens:
        letter_ct += len(i) * 10


    letter_ct += len("onethousand")

    letter_ct += len(number_hundred)*900
    return letter_ct


def run_it_three():
    ninetynine = 854
    letter_ct = 0
    for i in number_ones: # ["","one","two","three","four","five","six","seven","eight","nine"]
        letter_ct += len(i)*100


    letter_ct += len(number_hundred)*100 + ninetynine*10
    return letter_ct

# ninetynine is 854

print(run_it_one(1000))
#print(run_it_two())
#print(run_it_three())
