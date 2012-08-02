'''

Intro to Arguments


Arguments are things that you can pass onto your program when you start it, from the commandline. EG, instead of prompting for a name later, you could pass it as:

python program.py MyName

'''

import sys # just declares we want to use some stuff from the sys library, needed

print sys.argv # this is the list that contains all of the arguments passed onto python

print sys.argv[0] # in 99% of cases, this will be the name of your program (in above, "program.py")

print sys.argv[1:] # all the arguments you will be able to use as a programmer

'''

A few Notes:
- Arguments are always stored as strings regardless of what they are
- You need to be aware of users not passing on the arguments you want them to and telling them to send you what you want if they don't.

'''
