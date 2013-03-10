'''

An Introduction to For Loops

Python Forloops will loop through a list and perform an action with each member

'''

l = ["Hey", "There", "Everybody"]

for word in l: # note that 'word' can be anything you want (except a keyword), it's just like a temporary variable name
    print word,

# range is a function which can produce lists with a set of numbers
print range(5) # Produces list with numbers 0 -> 4 (ie: 5 members)
for i in range(5):
    print i # Will print 0, 1, 2, 3, 4 (ie: It will loop through that area of code 5 times

print range(1,5) # Like indexing, will slice, so will now start at 1 and go to 4 ([1,2,3,4])
