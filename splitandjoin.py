#You are given a string. Split the string on a " " (space) delimiter and join using a - hyphen.



def split_and_join(line):
    list = line.split(" ")
    new_line = "-".join(list)
    return new_line



s= "This is Sparta"
print(split_and_join(s))
