'''

A basic walkthrough of defining a class

'''


class Boy: # define a class with class just as you use def with functions.
    house = 'AAA' # fictional house - just set variables as you would normally
    tutor = 'BBB'
    form = 2
    

test = Boy() # assign a new object just as you would any other variable (string, integer, etc.), note the () on the end of Boy, it'll become clear why this is later but for now, don't leave them off.

print "The Test Boy is in Form: " + str(test.form) + ", in the house: " + test.house + ", with tutor: " + test.tutor
