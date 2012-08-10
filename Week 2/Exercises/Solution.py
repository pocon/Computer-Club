'''

A simple solution to the challenge, but with a few teaching points.

A few things:

1. sort() - sorts a list from the lowest to highest number and adds together the integer members of a list to determine their order if they are list-ceptioned. Note it won't sort the lists within lists automagically.

2. type() - gets the type of what something is (eg: list, int, string).

3. list - special python keyword which refers to lists in general

'''

l = input("Type In a List To Check: ") # input allows us to type in a list and have it become a list, rather than a string

def listSort(l):
    for m in l: # m is set as the member of the list and it just loops through the list with that.
        if type(m) == list: # if the member is another list
            listSort(m) # Run the whole sorting process on that list, so it's sorted (including any lists it contains)
    
    l.sort() # finally, sort the topmost list
    return l 

print listSort(l)

