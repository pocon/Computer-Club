'''

Intro to functions within classes

Just as we can nest variables in classes, we can do the same with functions, to act on themselves, with the self keyword.

'''



class Boy: # define a class with class just as you use def with functions.
    house = 'AAA' # fictional house - just set variables as you would normally
    tutor = 'BBB'
    form = 2

    def fancy_form(self): # Note: The self keyword has to be used in _every_ function that is defined in a class. It just refers to itself, or the object that it is (ie: self.house gives 'AAA' here)

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

    

test = Boy() 

print "The Test Boy is in Form: " + test.fancy_form() + ", in the house: " + test.house + ", with tutor: " + test.tutor

test.form = 5 # You can change variables within classes, they aren't set

print "The Test Boy is in Form: " + test.fancy_form() + ", in the house: " + test.house + ", with tutor: " + test.tutor
