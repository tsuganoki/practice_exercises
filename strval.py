"""In the first line, print True if  has any alphanumeric characters. Otherwise, print False.
In the second line, print True if  has any alphabetical characters. Otherwise, print False.
In the third line, print True if  has any digits. Otherwise, print False.
In the fourth line, print True if  has any lowercase characters. Otherwise, print False.
In the fifth line, print True if  has any uppercase characters. Otherwise, print False."""

s = "6$%^#"

alph = False
alphanumeric = False
digits = False
lowercase = False
uppercase = False

if len(s) < 1000:

    for l in s:

        if l.isalpha():
            alph = True
        if l.isdigit():
            digits = True
        if l.isalnum():
            alphanumeric = True
        if l.islower():
            lowercase = True
        if l.isupper():
            uppercase = True

print(alphanumeric)
print(alph)
print(digits)
print(lowercase)
print(uppercase)
