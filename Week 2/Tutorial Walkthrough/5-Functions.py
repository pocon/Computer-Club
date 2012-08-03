'''

Intro To Functions


Functions
=========

Functions are simply a block of code that you may want to use some time in the future. Rather than copying and pasting the code or only slightly modifying it, you can just refer to it...

'''

def giveTen(): # def is for 'define' and simply means that you're creating a function called giveTen (can call it whatever you want, exactly the same restrictions as variables). Note the (). This is key to a function
    return 10 # will 'return' the value of ten, so when you call this function, you get back 10

n = giveTen() # n is now 10 (just the same as n = 10), note the () on the end
print n

def addOne(x): # Variables can be added in the brackets to 'pass on' inputs, so the function can do more interesting stuff and change based on what you wrote
    return x + 1

o = addOne(9) # passes 9 onto addOne, so x = 9 in addOne
print o

def addTogether(x,y): # Multiple Arguments are fine.
    return x + y

p = addTogether(10,12) # passes on x = 10 and y = 12 to addTogether (which is which is based on order you pass them in)
print p

q = addTogether(y=8, x=9) # can specify which variable you want to set as each argument, so order doesn't matter
print q

def addTogetherOrAddOne(x, y=1): # where a variable is set to equal something else, this is set to its default (if you don't provide another value for y, it'll automatically be 1)
    return x + y

r = addTogetherOrAddOne(3,1)
s = addTogetherOrAddOne(3)
print r,s # are exactly the same
