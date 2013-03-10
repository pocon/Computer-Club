'''

An intro to class initialisers.

It's all well and good we can change values later but if we're adding in a bunch of boys, why can't we just pop their values straight in? That's what the __init__ method is for and that's why we use () when initialising a function.

The __init__ function is called the initialiser as it 'initialises' or 'starts' the object up with data

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

    

test = Boy('AAA', 'BBB', 5, "John", "S", "Citizen") 

print test.fancy_name() + " - Form: " + test.fancy_form() + ", in the house: " + test.house + ", with tutor: " + test.tutor

j = Boy(fname="John", initial="S", lname="Citizen", form=5, tutor="BBB", house="AAA") # You can specify which argument is which (this works for any function, the names have to match up with the ones you use in the function definition)

print j.fancy_name() + " - Form: " + j.fancy_form() + ", in the house: " + j.house + ", with tutor: " + j.tutor


