'''

An Introduction to Lists

'''

t = [] # lists are marked by square brackets, this is an empty list
print t

t = [2,4,5,2,1,23,34] # lists are a series of objects which are seperated by commas
print t

t = [2,"test", 3] # lists can contain different types of objects

print t[0] # Accesses the First Item in the List (the first item is at 0, not 1. This is key) -> in this case this is 2
print t[2] # Access the third item in the List (in this case 3)
print t[0:1] # Accesses the First Through to Second Items in the list
print t[:1] # Same as above. Leaving out the first number defaults to 0 (or the first item)
print t[1:] # Accesses everything in the list from the First item on (through to the last item)

# Handily, you can access strings as though they were lists and each of the members of the list are the characters, or letters of the string:

t = "Hello World"
print t[0] # is 'H' (The First letter of the String)
print t[6:] # is "World"

# Another useful string method is split which splits the string up by the string you provide as a seperator, and puts each seperate part as a member of a list:

g = t.split(" ")
print g # Will give ["Hello", "World"]
print g[1] # "World"

# the len() function when called on a list will give the number of objects in that list. You could think of strings as a special list of characters.

print len(t)
