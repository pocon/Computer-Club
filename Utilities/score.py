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
f = open(sys.argv[1], 'r')
for line in f.readlines():
    for char in line:
        if char != ' ' and char != '\t' and char != '\n':
            score += 1
        if char == '\n':
            score += 3

print "Golf Score: ", score
