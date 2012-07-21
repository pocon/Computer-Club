'''

Basic Manipulation of Strings

'''

text = "Hello World"

# Note: You Cannot Perform the integer manipulation on strings as you can't add numbers to a phrase!

num = str(23) # This is equivelant to num = "23", 23 is a string now, not a number, that means you can't add to it numberically but it's the same as any other string (like text)

print text + " " + num # Adding strings merges them together to form a Super String (here it gives "Hello World 23")

text += num # Same as integers, equivelant of text = text + num, now text = "Hello World23"

# Note that subtraction doesn't work for strings, nor does division nor raising to a power (**) nor mod (%)

t = text * 10 # makes 10 Copies of Hello World, back to back into one string
print t

# Some Special String Stuff Related to Printing:

print 'Hello', 'World' # Will print 'Hello World', it adds the two together, adding a space in between.
print 'Hello \n World' # \n is newline carriage meaning where you put it, the next words go onto a new line. Equivelant of having a print statement for "Hello", then one for "World"
print 'Hello \t World' # \t is a tab. equivelant of hitting the tab key inside Hello <tab> World
print 'I can\'t Do it' # if you type the apostrophe into can't without the \, python will think this is to close the string and cause problems as the rest of the string isn't enclosed. The \ 'escapes' the ' meaning that python shouldn't use it to close the string.
print "He said, \"Hey Dere\"" # works for " as well
print "One Line",
print "Same Line" # Adding a comma between print statements suppresses the creation of a new line, so they stay on the same line
