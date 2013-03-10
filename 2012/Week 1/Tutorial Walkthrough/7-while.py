'''

An Introduction to Program Flow with while statements

While Statements simply execute a block of code and keep looping through it until the boolean expression becomes False

'''

a = 6

while a != 0: # Tab after to ensure python knows it's part of the while "block"
    print "Hello"
    a -= 1

while True: # Will forever print. Endlessly. Until you kill the program (CTRL-c)
    print "Forever"
