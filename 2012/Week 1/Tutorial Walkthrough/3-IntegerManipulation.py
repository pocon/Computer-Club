'''

Basics of Manipulating Integers Once Set

'''

a = 1
b = 2
c = a + b # c now equals three.

a = 2
print c # Note that c is still three because it doesn't update when you change the other variables, it uses whatever the contents of those variables were before

a = a + 1 # You can also refer to the same variable you're assigning to. It uses the value of a before it's updated.
print a # a is 3 (it has been incremented by 1)

a += 1 # Shorthand for a = a + 1. Says "Take a and increment it by one"
a -= 1 # Subtraction works just the same
print a # a is 3 (we added 1 and then subtracted 1)

# Note that at this point, a = 3 and b = 2

c = a * b # '*' is the multiplication operator, it's the asterisk found above 8 on most keyboards
print c # Should be 6

c = c / b # '/' (forward slash) is the division operator
print c # Should be 3

print 10 / 3 # Gives 3, not 3.333... as python performs floor division on integers. Ie: if you take in two whole numbers, it will give out a whole number. Basically, if both inputs to the "/" operator are integers, it discards the fractional part of the result.
print 10.0 / 3 # Gives 3.333... as one of the numbers is a float (has a decimal place)

c = a ** b # '**' means "to the power of", 
print c # Should be 9 (3 squared)

# Shorthand works here too (but is more rarely used):
c *= a
c /= a
c **= a

print 30 % 2 # Modulus Operator (Clock Arithmetic). In reality: The remainder if 30 is divided by 2 (obv. 0)
print 31 % 3 # Will give 1 as 31/3 is 10 and a remainder of 1
