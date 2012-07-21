#!/usr/bin/python
'''

Basic 'Accounting' App (basically a calculator with + and -) which holds an account and transactions taken place.

'''

transaction_log = []
money = input("How Much Money Do You Have?: ") # As a Starting Point
transaction_log += ["Added " + str(money) + " To Account"]

print "There Are Four Commands: \n\t * pay <amount> \n\t * steal <amount> \n\t * balance \n\t * log"

while True:
    action = raw_input("What Would You Like To Do?: ")
    cmd = action.split(" ")[0].lower()
    if cmd == 'pay':
        money -= int(action.split(" ")[1])
        transaction_log += ["You Paid " + str(action.split(" ")[1])]

    elif cmd == 'steal':
        money += int(action.split(" ")[1])
        transaction_log += ["You Stole " + str(action.split(" ")[1])]

    elif cmd == 'balance':
        print "Your Balance Is: ", str(money)

    elif cmd == 'log':
        print "\n".join(transaction_log)

    else:
        print "Sorry, I didn't understand that command, please try again!"
