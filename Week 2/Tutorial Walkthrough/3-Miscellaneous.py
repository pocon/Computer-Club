# Some Handy tips and tricks that you can use involving the basic code constructs

# The notation if variable_name : is exactly the same as if variable_name==True : This is useful in making your code cleaner, more efficient and less redundant

a=True
if a==True:
 print "Hi!"
if a:
 print "Hi!"

# You can put the block on the same line as the if statement if it's only one line. This is especially helpful in challenge questions where newlines are to be avoided at all costs. You can also do this with elif and else statements.

if 10>6: print "Hi!"

# is the same as...

if 10>6:
 print "Hi!"

# The print statement by itself inserts a new line

print

# The print statement auto-inserts a new line after printing something by default

a="Hi!"
print a

# Placing commas between strings passed to the print statement adds a space between them

a="My favourite TV show is"
print a,"Play School" # Disclaimer: Tutorials are for educational purposes only and do not necessarily reflect the personal views of the creator of this document.

# Placing a comma at the end has the useful effect of suppressing the new line

print "There shouldn't be a new line after this",
print "See?"

