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

class Score:
    def __init__(self, file):
        self.SetScore(file)
        self.SetName(file)

    def SetScore(self, file):
        self.score = 0
        f = open(file, 'r')
        for line in f.readlines():
            l = line.strip()
            if not l.startswith("#"):
                for char in line:
                    if char != ' ' and char != '\t' and char != '\n':
                        self.score += 1
                    # NEED TO FIX \n. if we just increment by 3, comments are counted as 3



    def SetName(self, file):
        linenum = 0
        f = open(file, 'r')
        l = f.readline().strip()
        if l.startswith("#"):
            self.name = l[1:] # Ignore the hash and save the name
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
        for score in self.scores:
            print score.name, score.score
        
if __name__ == '__main__':
    board = Leaderboard('files/')
    board.output()

