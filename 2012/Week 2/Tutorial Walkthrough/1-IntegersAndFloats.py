# An integer is a whole number. ...-2,-1,0,1,2... Assign like any other variable

a=1

# You can carry out arithmetical operations on integers with +, -, *, /, % and brackets for order of operations

# Remember that division "/" when done with two integers is floored, ie it drops the fractional part

b=7
print a/b

# Remember how +=, -=, *= and /= notation is an abbreviated form

c=2
c=c+1
print c # should get 3

# This is the same as
c+=1
print c # should get 4

# Floating point numbers (floats for short) represent numbers with a decimal point. You can use all the normal arithmetical operators on them.
# Floats however are a different DATA TYPE. Data types are different types of object as viewed by Python, such as strings, ints, floats, lists etc.

# A note on division

print 3/4.0 # If just one of the operands is a float, python will perform floating-point division (ie normal division) on the values

# The input() function. Technically this funcation takes in any user input and automatically parses its data type. For example, if I type in [1,5,2,4] to an input() prompt, it stores it as a list. If I type in 3, it stores it as an int. If I type in 3.0, it stores it as a float. However as it means we can type a number straight in without quotes, we often use it to accept numerical input

# A simple addition program

int1=input()
int2=input()
print int1+int2
