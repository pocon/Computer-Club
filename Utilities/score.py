'''

Code Challenge Scorer: Lower is Better
-> Whitespace (' ') is ignored
-> Tabs are ignored
-> Newlines count for THREE POINTS (v. Bad)

How to Use:
Place this file inside the directory that contains your challenge solution. Then run python scorer.py <solution.py> where solution.py is what you named your challenge solution.

'''

import sys

score = 0
c = 0
f = open(sys.argv[1], 'r')
# Counter for line number.
linenum = 0
# Name variable, outside for scope (Not sure if it applies in python)
name = ''
for line in f.readlines():
    l = line.strip()
    linenum += 1
    # Check for comment, if line starts with comment then ignore.
    if linenum == 1:
        if l.startswith("#"):
            # Ignore the hash and save the name
            name = l[1:]
        else:
            # No name means its invalid. Return an error message.
            print 'You must include your name at the top in the form: #John Doe'
    elif l.startswith("#"):
        # KNOWN BUG: If you comment, you still get charged the three points from the previous line, as long as a comment is not the last line of the file the score adjusts its self
        c += 1
    else:
        for char in line:
            if char != ' ' and char != '\t' and char != '\n':
                score += 1
            if char == '\n':
                score += 3

# Output is the name and the score. This needs to be made into a class and then sorted/written. Possibly as an array of some sort?
print "Challenge Score for " + name + " (Lower is Better): ", score
# I am counting the comments because I have to do something
print "Comments: ", c
