import random

def roll():
    return random.randint(1,6)

d1 = roll()
d2 = roll()

print "Die 1:", str(d1)
print "Die 2:", str(d2)
print "Total:", str(d1 + d2) 
