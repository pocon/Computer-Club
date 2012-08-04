'''

More Advanced Slicing Techniques

'''

l = [0,1,2,3,4,5,6,7]

print l[4:5] # Gets 5th item from the list (indexing starts from 0)

'''

Important to Note: Slicing isn't choosing the items in the list, it's about dividing the list or slicing the list. In l[4:5], imagine a cursor is placed four items in, then it's moved to the fifth position, and what it's gone over is what's returned. In other words, you're selecting around the list not the items themselves (hence why the 5th item is obtained, but not the 6th):

 +---+---+---+---+---+
 | H | e | l | p | A |
 +---+---+---+---+---+
 0   1   2   3   4   5
-5  -4  -3  -2  -1

"One way to remember how slices work is to think of the indices as pointing between characters, with the left edge of the first character numbered 0."

'''

print l[-1:-3] # returns the last two members of the list (if you use negatives, it starts from the end, see above diagram).

print l[:4] # equals l[0:4], means to get everything up to the 4th slice position

print l[2:] # Means to get everything from the second slice on: l[2:len(l)-1]

print l[::1] # same as l. the Third position is step, meaning how much to advance by each time. See next line for eg.

print l[::2] # will get every second member in list (as it jumps by 2 each time, skipping 1 item)

#Note: slicing defined as l[start:end:step] where start is the position you start to slice at, end is where you stop and step is the amount by which you move.
# Defaults: start -> 0, end -> last item in list (ie: len(l)-1), step: 1

print l[2:6:2] # will get every second item between the 3rd and 7th items.

print l[::-1] # will print the reverse of the list as will step back through all of the items of the list
# It will go: l[-1], l[-2], l[-3] and so on.

# Note all this works for strings as well:

t = "Hello World"

print t[2:7:1]
print t[::-1]
