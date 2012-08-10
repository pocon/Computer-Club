#Encryption Challenge
##Prerequisites:
All people attempting this challenge should have completed:
* Week 2 Excercise 5 (simple logon program)
* Peter's Caesar Shift challenge

##Objectives:
* Your program should be able to store all login information in a text file (exactly like the logon excercise)
* You should offer a registration or logon page,
    * Registration should ask for a username and password (which is to be entered twice for confirmation)
    * If the username is already taken, or the re-entered password is incorrect, ask them to re-enter it
    * Logging in should simply print a welcome message and your username
    * To ensure security, the password in the text file **must not** be unencrypted
    * If logon details are incorrect, print a nice error
    
##The Challenge: 
1. Have all passwords encrypted before being transferred into the text file
2. Have the program pick a *random* key for the caesar shift, or use the key in the text file(if a logon file is there)
3. The program must be in ONE python script, and must make use of Functions as explained in the Week 2 tutorials

####The Due date for this program is 14AUG2012