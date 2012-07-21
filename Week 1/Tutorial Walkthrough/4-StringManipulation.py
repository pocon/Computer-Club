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

