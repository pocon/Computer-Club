# Casting is the art of converting a variable from one data type to another. You already have learnt of 1 function used for casting (2 if you did the exercises) - int() and float()

# int() takes the argument and tries to return an int, if possible

print int("94")+1 # If the string just contains an int, all is well. Should get 95

print int("This is clearly not an int") # Strings that can't be converted to ints throw errors

print int(99.5)+1 # int will chop off the fractional part of floats passed to it. Should get 100.

print int("99.5") # Interestingly valid floats as strings also throw errors

# float() takes the argument and tries to return a float, if possible

print float(34) # Passing an int to float() simply returns the float equivalent (in this case, 34.0)

print float("This is clearly not a float") # Obviously this will also throw an error

print float("34") # Interestingly unlike int() float will play nicely with ints as strings and return 34.0

# str() takes the argument and returns it as a string

print str(34)

print str(375.92)

print str([5,3,1,3]) # str() is the cool kid, it will take most things and spit them out as strings (yes even lists)

# NB: Take care with data types!!! This is especially important when dealing with strings and ints, since they share operators (+ and *) that do different things depending on the operators they're fed

# String operands to "+" result in concatentation. Basically the 2nd string is stuck at the back of the first. In contrast + applied to integers just adds the numbers

print raw_input("First number to be added:")+raw_input("Second number to be added:") # This fail calculator gives 1+1=11. This is because raw_input() converts everything to a string

print int(raw_input("First number to be added:"))+int(raw_input("Second number to be added:")) # We should convert them to ints to get the right answer

print input("First number to be added:")+input("Second number to be added:") # Alternatively we could have just used input()
