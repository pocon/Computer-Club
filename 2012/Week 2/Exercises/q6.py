import math # Gives us access to the standard math library, as per 8-math.py

def pythagoras(a,b):
 return math.sqrt(a*a+b*b)

# Example program using this function

side1=input("Enter first side length: ")
side2=input("Enter second side length: ")
print pythagoras(side1,side2)
