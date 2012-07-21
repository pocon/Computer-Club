'''

Script Which Generates a Timestable to desired amount

'''

to = input("What Number Do You Want To Generate The Table To?: ")
up_to = 1

print "".ljust(3), 
for i in range(1,to):
    print str(i).center(3),
print

print "".ljust(3),
for i in range(1,to):
    print "---".center(3),
print

while up_to <= to:
    print (str(up_to)+"|").ljust(3),
    for i in range(1,to):
        print str(i*up_to).center(3),
    print

    up_to += 1
