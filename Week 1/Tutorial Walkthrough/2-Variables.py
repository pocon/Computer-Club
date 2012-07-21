'''

A Basic Run Through Assignment and variables

'''

# Strings (A set of words or phrases)

text = 'Hello World' # This 'assigns' the variable text as 'Hello World'. That is, text is set to now refer to 'Hello World', as x = 3 in maths means that x has the value of 3
text = "Hello World" # A string can be contained in double or single quotes, it doesn't matter

print text # This prints the contents of the variable 'text', or displays them on the console

# Integers (Whole Numbers)

number = 10
print number

# Floating Point Numbers (Like Decimals)

number = 10.1
print number

# Taking Input
n = raw_input("Type Your Name: ") # Will Produce a prompt on the command Line saying: "Type Your Name: " After the user types in a name and presses enter, the name they typed is set as n (as a string, regardless of whether they typed a number or not)

# Converting Strings to Numbers:
n = "23" # For example, if the user typed 23 for above
n = int(n) # turns it from "23" -> 23, so you can now manipulate it as a number (more on next page)