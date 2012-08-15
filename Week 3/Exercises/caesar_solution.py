# peterarenot

import sys

# Check for the correct number of arguments
if len(sys.argv) != 2:
    # Provide the correct usage of the program
    sys.exit("Correct usage is: python " + sys.argv[0] + " key")

k = sys.argv[1]

# Check if the argument provided is a number
while not k.isdigit():
    k = raw_input("That's not a number!\nPlease give a key: ")

# Cast k as an integer
k = int(k)

# Check that imput is positive int
if k <= 0:
    sys.exit("Please provide a positive integer as the key")

# Ask the user for a string
s = raw_input("Please give a string: ")

# Keep asking for a string if one was not given!
while s == "":
    s = raw_input("That's not a string!\nPlease give a string: ")

# Loop through string
for c in s:

    # Check if c is a letter
    if c.isalpha():
        
        # Check if c is an uppercase letter
        if c.isupper():

            c = ord(c)
            o = ((c + k) -65) % 26
            o += 65
            o = chr(o)

        # Must be lowercase
        else:

            c = ord(c)
            o = ((c + k) -97) % 26
            o += 97
            o = chr(o)

        # Print each character
        sys.stdout.write(o)

    # If not a letter must be number or punctuation
    else:
        sys.stdout.write(c)

# Print newline
sys.stdout.write("\n")