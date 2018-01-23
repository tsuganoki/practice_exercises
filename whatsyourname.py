a = input()
b = input()



def print_full_name(a, b):
    if len(a) > 10 or len(b) > 10:
        print("too long")
    else:
        print("Hello "+ a +" " + b + "! You just delved into python.")
print_full_name(a,b)
