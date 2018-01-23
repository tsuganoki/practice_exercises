""" a given index and then print the modified string.

Input Format
The first line contains a string, s .
The next line contains an integer i, denoting the index location and a character c separated by a space."""

def mutate_string(string, position, character):
    l = []
    l = list(string)
    l[position] = character
    new_string = "".join(l)
    return new_string
