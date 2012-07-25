Plan for Computer Club Week 1 (TUES 24 JUL 12 - 1:00 pm)
========================================================
## Installing Python ##
### Windows ###

Download from: http://www.python.org/getit/ and run the installer as per normal. 

Then, you'll need to set up the PATH variable to look in python to ensure you don't have to type out the full path each time:

> http://docs.python.org/using/windows.html#finding-the-python-executable:

"Windows has a built-in dialog for changing environment variables
(following guide applies to XP classical view): Right-click the icon
for your machine (usually located on your Desktop and called “My
Computer”) and choose Properties there. Then, open the Advanced tab
and click the Environment Variables button.

In short, your path is:

My Computer ‣ Properties ‣ Advanced ‣ Environment Variables
In this dialog, you can add or modify User and System variables. To
change System variables, you need non-restricted access to your
machine (i.e. Administrator rights)."

Then, find the PATH variable and add to the end of it (don't delete
the other stuff): ";C:\Python27"

Make sure the colon closes off the other one. Completely, PATH should
look like: "C:\WINDOWS\system32;C:\WINDOWS;C:\Python27"

Finally, .py files are just text files and can be edited with notepad but your life is 100x times easier using Notepad++. Just run the installer, available here: http://notepad-plus-plus.org/download/v6.1.5.html (first link)
After that, get cracking on the tutorial.

The Interpreter can be opened within a prompt (WinKey-r cmd) by typing python (assuming your path has been set correctly above). To run a file, cd to that file's directory and type python yourfile.py.

Type driveletter: to change to that drive. For example if I'm in my home folder in C:\ and my python program is in D:\ type d: and press enter.

From here type cd yourfolderaddress. Your prompt should change to the directory your python program is in (for example, D:\Files\Python> ) here you can type python yourfile.py to execute your program.

Any problems, ask the mailing list.

### Mac ###
Should come with python 2.7 installed. Load up a terminal and type 'python' and make sure it says 2.7.x near the top. If not, (eg: it says python 2.5 or something), update it with: http://www.python.org/getit/
Use any text editor for .py files. Python is launched by typing python into a terminal. A file can be run with python file.py

### Linux ###
Most distributions should ship with it by default. If not, search your repo or grab the tarball from above and compile (easy as pie, has makefile and all).


## Welcome To Computer Club ##
1. Plan on Learning Programming for the club over the next few terms
2. During Term III we'll learn Python (Programming Language)
3. During Term IV we'll write a major project amongst the whole group (start thinking of ideas)
4. By the end of this term, you will be fairly proficient in a major programming language (python), enough so you are capable of continuing learning yourself, or learn another language, as you will understand many of the difficult concepts

## Introductions ##
1. Introduce Leaders: Will, Alex and Patrick
2. Get an idea of technicality of Users and Names (eg: Who's programmed before, what in? What OS do you run?)


## Introduction to Programming and Python ##
1. Programming is About Instructing a computer to do what you want. At this level, that's inserting data into memory and performing operations on that data.
2. Python is an interpreted language (No need to compile, done on the fly) which has risen to importance recently (past decade). 
   i. Very easy to learn
   ii. Excellent documentation
   iii. Used By: NASA, Google (a lot), Yahoo!, Battlefield II, IBM, etc.

## Installing Python and Getting Setup - http://python.org/download/ ##
1. We're using Python2, because nobody likes 3
2. Show windows installer
3. Macs have python by default but you should update to 2.7 by using the Mac installer
4. *Nix/Solaris: Can compile from source or should be in 99% of repos

## Running Python ##
1. Show interpreter: "Hello World"
2. Show how to launch files (using text editor and launch with python filename.py)

## An Introduction to Assignment and Variables (if Time) ##
1. simple a = 1, etc.

# For Next Week: #
1. Setup Python at home. Work out how to both use the interpreter and launch files
2. Read Through: https://github.com/pocon/Computer-Club/tree/master/Week%201/Tutorial%20Walkthrough

## Additional Reading ##
http://docs.python.org/tutorial/introduction.html
http://openbookproject.net/thinkcs/python/english2e/ch01.html
http://openbookproject.net/thinkcs/python/english2e/ch02.html
