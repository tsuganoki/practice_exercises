
#You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.



def swap_case(s):
    swap = ""
    for l in s:
        if l.isalpha() == False:
            swap = swap + l;
        elif l.isupper() == True:
            swap = swap + l.lower()
        elif l.islower() == True:
            swap = swap + l.upper()
    return swap


print(swap_case("This is DOCTOR"))
