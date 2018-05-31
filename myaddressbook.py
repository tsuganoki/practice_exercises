from difflib import SequenceMatcher

def similar(a,b):
    return SequenceMatcher(None, a, b).ratio()

def sanitize(my_string):
    sanitString = ""
    for i in my_string:
        if i.isalnum():
            sanitString += i
    return sanitString

def sanitNum(my_num):
    sanitString = ""
    for i in my_num:
        if i.isnumeric():
            sanitString += i
    return sanitString

def santitLongStr(my_long_string):
    sanitString = ""
    for i in my_long_string:
        if i.isalnum() or i == " " or i == "," or i == "." or i ==":" or "\'":
            sanitString += i
    return sanitString




class Entry(object):
    def __init__(self,fname,lname,company,street,city,state,zip,country,phone,memo):
        self.fname = fname
        self.lname = lname
        self.fullname = " ".join([self.fname,self.lname])
        #self.fullname = self.fname + " " + self.lname
        self.company = company
        self.street = street
        self.city=city
        self.state = state
        self.zip = zip
        self.cityAddress = ""
        for i in [self.city,self.state,self.zip]:
            if i != "":
                if i == self.city:
                    if self.state != "" or self.zip !="":
                        self.cityAddress += i +", "
                    else:
                        self.cityAddress += i
                        break
                else:
                    self.cityAddress += i +" "
        self.country = country
        self.phone = phone
        self.memo = memo
        self.allAttributes = [self.fname,self.lname,self.fullname,self.company,self.street,self.city,self.state,self.zip,self.country,self.phone,self.memo]



    def displayEntry(self):
        #print(self.fname +" " + self.lname)
        self.book[key].allAttributes = [self.fname,self.lname,self.fullname,self.company,self.street,self.city,self.state,self.zip,self.country,self.phone,self.memo]

        print(self.fullname)

        #if self.fullname != ""  : print(self.fullname)
        if self.company != ""   : print(self.company)
        if self.street != ""    : print(self.street)
        if self.cityAddress != ", ": print(self.cityAddress)
        """if self.city != "" and self.state != "" and self.zip != ""):
            print(self.city +", " + self.state + " " + self.zip)
        else:
            print("this will look a bit fucky")
        cityString = " ".join([self.city,self.state,self.zip])
        if self.city != "" and (self.state != "" or self.zip != ""):
            cityString = " ".join([self.city,", ",self.state,self.zip])
            print(cityString)
        elif cityString != "  " : print(cityString)"""

        if self.country != ""   : print(self.country)
        if self.phone != ""     : print("(" + self.phone[:3] + ")" + self.phone[3:6] + "-" + self.phone[6:])
        #if self.birthday != "" : print(self.birthday)
        if self.memo != ""      : print("Memo: " + self.memo)
        print()


class AddressBook(object):
    def __init__(self):
        self.book = {}
        self.keyCounter = 1
        self.online = True






    def editEntry(self,key):
        #fname,lname,company
        print()
        print("(N)name -- (C)Company -- (A)address -- (P)phone -- (M)memo --  (E)exit  ") #-- (A)address -- (P)phone -- (B)birthday -- (M)memo --
        field = input("Please make a selection: ")
        print()
        field = field[0].lower()
        if field == "n":
            self.book[key].fname = sanitize(input("Please enter the First Name or hit Enter to skip: "))
            self.book[key].lname = sanitize(input("Please enter the Last Name or hit Enter to skip: "))
            self.book[key].fullname = " ".join([self.book[key].fname,self.book[key].lname])
            return self.editEntry(key)

        elif field == "c":
            self.book[key].company = santitLongStr(input("Please enter the Company or hit Enter to skip: "))
            return self.editEntry(key)
        elif field =="a":
            self.book[key].street = sanitize(input("Please enter the street address or hit Enter to skip: "))
            self.book[key].city = sanitize(input("Please enter the City or hit Enter to skip: "))
            self.book[key].state = sanitize(input("Please enter the State or hit Enter to skip: "))
            self.book[key].zip = sanitize(input("Please enter the zip code or hit Enter to skip: "))
            self.book[key].country = sanitize(input("Please enter the Country or hit Enter to skip: "))
            for i in [self.city,self.state,self.zip]:
                if i != "":
                    if i == self.city:
                        if self.state != "" or self.zip !="":
                            self.cityAddress += i +", "
                        else:
                            self.cityAddress += i
                            break
                    else:
                        self.cityAddress += i +" "

            return self.editEntry(key)

        elif field =="p":
            self.book[key].phone = sanitNum(input("Please enter the phone number or hit Enter to skip: "))
            return self.editEntry(key)
        elif field =="m":
            self.book[key].memo = santitLongStr(input("Please enter a memo or hit Enter to Skip: "))
            return self.editEntry(key)

        elif field == "e":

            self.book[key].displayEntry()
            return self.book[key]
        else:
            print("I didn't understand that. Everything is broken now.")
            return self.editEntry(key)

    def addEntry(self):

        self.book[self.keyCounter] = Entry(fname="",lname="",company="",street="",city="",state="",zip="",country="",phone="",memo="")

        self.editEntry(self.keyCounter)

        self.keyCounter += 1




    def lookupCompany(self):
        term = sanitize(input("Please type a search term: "))
        results = []
        for key in self.book.keys():
            if similar(self.book[key].company.lower(), term.lower()) > .8:
                results.append(myBook.book[key])

        if results == []:
            print("No results found.")
        else:
            print("Results found for company " + term)
            for i in results:
                print(i.displayEntry())

    def lookupAny(self):
        term = santitLongStr(input("Please type a search term: "))
        print()
        results = []


        for key in self.book.keys():
            for attrib in self.book[key].allAttributes:
                if attrib.lower() == term.lower():
                    results.append(key)
                    break

        if len(results) == 0:
            print("No results found matching \"" + term +"\"")

        elif len(results) == 1:
            print(str(len(results))+ " Result found matching \"" + term +"\"")
            key = results[0] # this is only to make it easier for future me
            self.book[key].displayEntry()
            #print("debug -- Key: ", key)
            editYN = sanitize(input("Would you like to edit this entry? Y/N "))

            if editYN.lower() == "y":
                #print("Edityn = ",editYN)
                return self.editEntry(key)

        else:
            print(str(len(results))+ " Results found matching \"" + term +"\"")
            print()
            for i in results:
                self.book[i].displayEntry()
            print("To edit an entry, please enter a more unique Search Term. ")
            print()

        #



    def useBook(self):
        while self.online:
            print("Please make a selection: ")
            choice = sanitize(input("(A)Add New Entry -- (S) Search --  (E)Exit ")).lower()
            if len(choice) < 1:
                print("Sorry, that's not a valid selection. Please try again. ")
                return self.useBook()

            elif choice[0] == "a":
                self.addEntry()
            elif choice[0] =="s":
                self.lookupAny()
            elif choice[0] == "e":
                self.online = False
                break
            else:
                print("Sorry, that's not a valid selection. Please try again. ")
                return self.useBook()
            self.useBook()

myBook = AddressBook()

myBook.book["a"] = Entry(fname="Alice",lname="Smith",company="Google",street="132 Main St",city="",state="PA",zip="14202",country="",phone="4323321234",memo="Vegetarian")
myBook.book["b"] = Entry(fname="Bob",lname="Jones",company="Twitter",street="42 El Camino",city="Palo Alto",state="CA",zip="94105",country="",phone="",memo="")
myBook.book["c"] = Entry(fname="Eve",lname="Doe",company="SpaceX",street="5321 3rd Ave Apt 203",city="Mountain View",state="CA",zip="09606",country="",phone="",memo="She's very cute")
myBook.book["d"] = Entry(fname="Elon",lname="Musk",company="Boring Company",street="",city="Mountain View",state="",zip="",country="",phone="",memo="")
myBook.book["e"] = Entry(fname="Katherine",lname="Hepburn",company="",street="",city="Hollywood",state="CA",zip="90210",country="",phone="",memo="")

myBook.useBook()
#myBook.lookupAny()
#myBook.editEntry("a")

"""myBook.book[0].displayEntry()
myBook.book[1].displayEntry()
myBook.book[2].displayEntry()
myBook.book[3].displayEntry()
myBook.book[4].displayEntry()"""


"""
for i in myBook.book.keys():
    if myBook.book[i].company == "SpaceX":
        print(myBook.book[i].fullname)"""

#myBook.lookupCompany("SpaceX")
