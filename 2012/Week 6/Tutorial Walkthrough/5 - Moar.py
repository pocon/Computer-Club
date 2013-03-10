'''

Some further functioning that allows you to add someone new to a house

'''

class Boy: # define a class with class just as you use def with functions.
    def __init__(self, house, tutor, form, fname, initial, lname):
        self.house = house # Note: We don't have to setup the variable first, we can just go self.anything = anything.
        self.tutor = tutor
        self.form = form
        self.fname = fname
        self.lname = lname
        self.initial = initial

    def full_name(self):
        return self.fname, self.initial, self.lname

    def fancy_name(self):
        return self.fname[0].upper() + "." + self.initial.upper() + "." + self.lname.upper()

    def fancy_form(self): 
        if self.form <= 3:
            return "I" * self.form

        elif self.form == 4:
            return "IV"

        elif self.form == 5:
            return "V"
        
        elif self.form == 6:
            return "VI"
        
        else:
            return "Error"


class House:
    members = []
    name = "AAA"

    def add_boy(self, form, tutor, fname, initial, lname):
        b = Boy(form=form, tutor=tutor, fname=fname, initial=initial, lname=lname, house=self.name)
        self.members += [b]

    def tutorial_list(self, tutor):
        tut = []
        for member in self.members:
            if member.tutor == tutor:
                tut += [member]

        return tut

h = House()

h.add_boy(form=2, tutor="BBB", fname="John", initial="C", lname="Smith")

h.add_boy(form=2, tutor="CCC", fname="Bob", initial="J", lname="Brown")

h.add_boy(form=2, tutor="BBB", fname="Linus", initial="B", lname="Torvalds")

print "Tutorial List For BBB"
print "====================="

for member in h.tutorial_list("BBB"):
    print member.fancy_name() + " - Form: " + member.fancy_form() + ", in the house: " + member.house + ", with tutor: " + member.tutor

    
