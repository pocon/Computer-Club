'''

A Basic Run Through Assignment and variables

'''

# Strings (A set of words or phrases)

text = 'Hello World' # This 'assigns' the variable text as 'Hello World'. That is, text is set to now refer to 'Hello World', as x = 3 in maths means that x has the value of 3
text = "Hello World" # A string can be contained in double or single quotes, it doesn't matter

print text # This prints the contents of the variable 'text', or displays them on the console

''' 

Can I name variables anything?
-> Almost Anything except for python keywords (that is, words reserved for python because they do other things)
-> For example, it would not be possible to name a variable print as python will just be confused
-> A list of keywords can be found here: http://docs.python.org/reference/lexical_analysis.html#keywords
-> Also, your variable name can't contain a number at the start of it, but it can contain a number within or at the end of the name. For example, 3abc is an invalid name, but ab3c and abc3 are legit

'''

# Integers (Whole Numbers)

number = 10
print number

# Floating Point Numbers (Like Decimals)

number = 10.1
print number

# Taking Input
# Note that n can be any arbitrary variable you assign to. It's not "Type Your Name: " that stores the value, it's n. See above with: "can I name variables anything"
n = raw_input("Type Your Name: ") # Will Produce a prompt on the command Line saying: "Type Your Name: " After the user types in a name and presses enter, the name they typed is set as n (as a string, regardless of whether they typed a number or not)

n = input("Type a Number: ") # Will compute the expression of whatever somebody types in there. In the most basic of uses, means that if you type a number, its type will be int.

# Converting Strings to Numbers:
n = "23" # For example, if the user typed 23 for above
n = int(n) # turns it from "23" -> 23, so you can now manipulate it as a number (more on next page)
