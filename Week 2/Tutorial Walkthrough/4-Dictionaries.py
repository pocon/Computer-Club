# Dictionaries are quite similar to lists, except that lists use INTEGERS as indicies (ie mylist[0], mylist[1]). Dictionaries can use any immutable data type as an index (this means strings, ints, and "tuples" (which you will learn about once that tutorial gets pushed)). For example, you could create a mapping from strings to integers.

mydict={} # Dictionaries use curly brackets as syntax. This is an empty dictionary

mydict["one"]=1 # Here our index is a string, and we've mapped it to an int (1)

print mydict["one"]
print mydict # You can use the print statement as with lists

#Special names: in a dict, the indices are known as KEY, and the value assignments are KEY-VALUE pairs (eg above "one" and 1 are a key-value pair). When print is called on it, colons are used to denote pairings and pairs are separated by commas
# ie {"one":1,"two":2} etc

mydict2={"one":1,"two":2,"three":3,"four":4} # You can also create dicts with this colon comma syntax

print {"one":1,"two":2,"three":3}=={"two":2,"three":3,"one":1} # Notice how we don't care about order, these are the same dict as the mapping is the same

del mydict2["two"]
print mydict2 # You can delete a key-value pair using del.

print len(mydict2) # len() returns the number of key-value pairs in a dict

# A quick and dirty introduction to methods and objects.
# Up till now you've mainly learned about functions that can be called by themselves. Functions such as len() and stuff like print can be thought of as "general purpose" functions that you can call and have do stuff. In contrast, with dicts you can use the following notation:

print mydict2.keys()

# Appending ".keys()" to a dict variable returns a list of all the keys in the dict (which is passed onto print in our example). In this case, keys() is a special type of function known as a method; notice how it is in a way associated with mydict2 and is not general like len(). mydict2 is known as the OBJECT. You'll learn more about objects and methods later.
# The key thing here is to realise that keys() is associated specifically with the mydict2 construction. If it were a general purpose function like len(), the notation would have been keys(mydict2).

print mydict2.values() # values is another method that returns the list of the values in the dictionary

print mydict2.items() # items is a method that returns a list of tuples of key-value pairs. Since you don't know about tuples yet, this isn't of that much use

print mydict2.has_key("one") # the has_key method returns True if the key appears in the dictionary and False if not

print mydict2.get("one",50)
print mydict2.get("blahblah",50) # The get method looks at the first argument ("one" or "blahblah" in this example); if it is a key in the dictionary, it returns the assciated value, if not it returns the second argument (50 in both cases)
