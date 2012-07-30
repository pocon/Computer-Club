'''
Code Challenge Scorer

Scorer rules:
  -> Whitespace (' ') is ignored
  -> Tabs are ignored
  -> Newlines count for THREE POINTS (v. Bad)
  -> Comments that take up a whole line (ones that start at the first character) are ignored
  -> Name must be on first line in format (#First Last)

How to Use:
  Place this file in a folder and in the same folder create a folder called "files". Put all the .py files in this folder. Now run score.py.
  OR
  Give a py file to score and it will print the score.
  OR
  Specify a folder (i.e. Bob/solutions/) and it will score the whole folder.
  
Authors:
  - pocon
  - blakedut2
  - peterarenot

'''

import sys
import os
import glob
import re

class Score:
    def __init__(self, file):
        self.setscore(file)
        self.setname(file)

    def setscore(self, file):
        self.score = 0
        f = open(file, 'r')
        inputloc = re.compile('input\(.*\)')
        ims = 0
        for line in f.readlines():
            l = line.strip()
            m = inputloc.search(l)
            if m:
                ims += len(m.group()) -9
            if not l.startswith("#"):
                for char in line:
                    if char != ' ' and char != '\t' and char != '\n':
                        self.score += 1
                    if char == '\n':
                        self.score += 3
        self.score -= ims


    def setname(self, file):
        f = open(file, 'r')
        l = f.readline().strip()
        if l.startswith("#"):
            self.name = l[1:].strip()
        else:
            self.name = f.name


class Leaderboard:
    def __init__(self, folder):
        self.scores = []
        for infile in glob.glob(os.path.join(folder, '*.py')):
            self.scores += [Score(infile)]
        self.sort()

    def sort(self):
        self.scores = sorted(self.scores, key=lambda score: score.score)

    def output(self):
        with open('leaderboard.md', 'w') as f:
            f.write("# Challenge LeaderBoard # \n")
            f.write("<table><tr><th>Rank</th><th>Name</th><th>Score</th></tr> \n")
            for i, score in enumerate(self.scores, start=1):
                formatted = "<tr><td>%d</td><td>%s</td><td>%d</td></tr> \n" % (i, score.name, score.score)
                f.write(formatted)
                
            f.write("</table>")
                
        
if __name__ == '__main__':
    if (len(sys.argv) > 1): # Check for arguments
        pa = sys.argv[1]
        if ".py" in pa:
            print Score(pa).name + ": ", Score(pa).score # If python then score and print
        else:
            board = Leaderboard(pa) # If not python assume is folder
            board.output()
    else:
        board = Leaderboard('files/') # If folder not specified use "files"
        board.output()

