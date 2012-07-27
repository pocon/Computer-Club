'''
Code Challenge Scorer

Scorer rules:
  -> Whitespace (' ') is ignored
  -> Tabs are ignored
  -> Newlines count for THREE POINTS (v. Bad)
  -> Comments that take up a whole line (start at first  character) are ignored
  -> Name must be on first line in format (#First Last)

How to Use:
  Place this file in a folder and in the same folder create a folder called "files". Put all the .py files in this folder. Now run score.py.
  
Authors:
  - pocon
  - blakedut2
  - peterarenot

'''

import sys
import os
import glob

# getScore counts the score of the file and returns an int
def getScore (file):
    score = 0
    c = 0
    f = open(file, 'r')
    for line in f.readlines():
        l = line.strip()
        # Check for comment
        if l.startswith("#"):
            # KNOWN BUG: If you comment, you still get charged the three points from the previous line, as long as a comment is not the last line of the file the score adjusts its self
            c += 1 #This is needed, if anyone knows a way to remove this then change it!
        else:
            for char in line:
                if char != ' ' and char != '\t' and char != '\n':
                    score += 1
                if char == '\n':
                    score += 3
    return score

# getName takes a file and returns it as a string or an errorcode of 1
def getName(file):
    linenum = 0
    name = ''
    f = open(file, 'r')
    for line in f.readlines():
        l = line.strip()
        linenum += 1
        # Check for comment, if line starts with comment then ignore.
        if linenum == 1:
            if l.startswith("#"):
                # Ignore the hash and save the name
                name = l[1:]
                return name
            else:
                # No name means its invalid. Return an error message.
                return 0

# Code to open files
path = 'files/'
for infile in glob.glob( os.path.join(path, '*.py') ):
    if getName(infile):
        print getName(infile) + ": ", getScore(infile)
    else:
        print "No name (" + infile + "): ", getScore(infile)
    