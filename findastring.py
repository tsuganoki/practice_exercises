"""
In this challenge, the user enters a string and a substring. You have to print the number of times that the
substring occurs in the given string. String traversal will take place from left to right, not from right to left.

NOTE: String letters are case-sensitive.

Input Format

The first line of input contains the original string. The next line contains the substring"""

def count_substring(string, sub_string):
    sub_len = len(sub_string)
    #print("sublength is " + str(sub_len))
    str_len = len(string)
    #print("string length is " + str(str_len))
    match = 0
    for i in range(str_len):
        #print("is this on?")
        if string[i:(i+sub_len)] == sub_string:

            #print(string[i:(i+sub_len)])
            match +=1


    return match





str1 = "baa baa black sheep"
str2 = "sheep"
str3 = "baa"
str4 = "omega"
str5 = "a"

print (str2,count_substring(str1, str2))

print (str3,count_substring(str1, str3))
print (str4,count_substring(str1, str4))
print (str5, count_substring(str1, str5))
