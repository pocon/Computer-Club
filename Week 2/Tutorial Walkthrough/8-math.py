# The standard python math library is a bit like sys; by importing the math library, you now have access to a range of functions that can perform mathematical operations, such as trigonometry, square roots, etc

import math # Just declares we want to use stuff from math, just like import sys

print math.sqrt(2) # I can now do square roots
print math.sqrt(4)

print math.log(2,10) # I can also do logarithms. Syntax = logarithm of first number (ie 2) to base 10
print math.log(3) # Giving only one argument returns the natural logarithm

print math.pi # I can also access useful mathematical constants
print math.e

print math.sin(math.pi) # I can access trigonometric functions
print math.cos(math.pi)
print math.tan(math.pi)
# NB: trigonometric functions in python deal in RADIANS. To convert from degrees to radians, use math.radians(x), eg

print math.radians(180)

# Radian angle measure is such that pi radians is equal to 180 degrees

print math.degrees(math.pi) # use math.degrees to convert from radians to degrees

# Some miscellaneous useful functions

print math.factorial(6) # You can do factorials

print math.floor(3.4) # and have access to floor and ceiling functions
print math.ceil(4.5)

# If for whatever reason you need access to more advanced mathematical constructions, such as hyperbolic trigonometry, error functions, gamma functions etc, please refer to the standard Python reference documentation, which provides an exhaustive reference for math and other standard libraries. If you want to play with complex numbers, use the cmath library.
