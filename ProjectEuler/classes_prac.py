from random import randint

class die(object):
    def __init__(self,num_sides):
        self.num_sides = num_sides

    def roll_die(self):
        return(randint(1,self.num_sides))

bones = die(6)

print(bones.roll_die())
