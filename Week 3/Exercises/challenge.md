# Caesar Challenge
This challenge is related to encryption and passwords on computers. You will create a script that encrypts a string and then prints out the encrypted version.

## About encryption
There are many different forms of encryption. The types that are used in modern computers are very complex and hard to break. This challenge involves one of the simplest ciphers, the Caesar Cypher.

This cipher involves rotating the alphabet around by a given number of characters (the key). The cipher was used by Caesar to send messages to his commanders that could not be read by the enemy. All he needed was to agree on a key before hand and then the message could be read.

So, the Caesar cipher is just rotating every letter in a given string (plaintext) by a certain number of places (the key) wrapping around if needed (if Z is moved one place it becomes A).
For example:
```
key = 13
plaintext: "Hello world!"
ciphertext "Uryyb jbeyq!"
```
This is a ROT13 cipher, as in the text is rotated 13 places. Would a ROT26 cipher be very secure?

## The challenge
You must (only if you wan't to though!) create a python program caesar.py that takes a integer as a key (either through the command-line or `(raw)input()`) then a string and prints the ciphertext!

An example could look like this:
```
>>> python caesar.py 13
Please give a string:
>>> Hello World!
Uryyb jbeyq!
```

## Here are the requirements:
- Must take a positive integer as an argument (or other input if you must)
- If the key is not a positive integer the program must print an error and either ask again or stop
- Must take a string as input
- If a string is not given you must ask again for a string or stop
- Must encrypt the string using the key and then print the ciphertext
- All punctuation (spaces, periods, commas) and numbers must remain
- All capitals must remain
- The cipher must wrap around (Z rotated by 1 is A)

## How to do it?

### Formula
Here is the formula:
`c=(p+k)%26`
Where c is a letter in the ciphertext, p is the corresponding letter in plaintext and k is the key. This formula may seem very complicated, much more so then it really is.

### ASCII
To complete this you are going to need to use the ASCII character table (http://www.asciitable.com/). Here you can see that "a" is represented by the int "97" and "A" by "65". How can you convert the character to the int value? Simply use `ord()`. Eg: `ord("a") == 97`
To convert back to a char use `chr()`
Eg: `chr(97) == "a"`

The formula requires you use the int values for each char (NOTE: A and a are different.)

### Iterating through strings
If you are given a string s, `s = "Hello"` then to iterate through it you must use a for loop.
Eg:
```
for c in s:
    # Do something with c
```
This gets each letter in "s" and calls it "c". So to print each letter out you would use `for c in s: print c`.

### Maintaining capitals
You will need to check if each character is a capital or a number or punctuation. To do this you need to use str functions
First, `import str` at the top of your file. Then you can call:
- `str.isalpha(c)` which returns True or False is the character c is a letter
- `str.isnumeric(c)` which returns True or false if the character c is a number
- `str.isupper(c)` which returns True or false if the character c is an uppercase letter

You are able to test for punctuation with these functions as well!

### Changing from ASCII to position in alphabet!
You will have to change from ASCII to the place of the char in the alphabet. So A will be 1 and Z 26 instead of 97 and 122. To do this you should take away from the ASCII value a certain amount to make 97 == 1 and 122 == 26 for lowercase and 65 == 1 as well as 90 == 1 for uppercase!
The output of the formula will therefor be out of 26 and must be changed to the ASCII value before printing.

### Printing without newlines
To print each character without a newline you must either append all characters to a string and print at the end or use `sys.stdout.write(c)` instead of `print(c)`.

# Done?
This solution is due on the 14th so you can ask questions on Tuesday or on the Google Group! I will tell you how to submit on Tuesday!

The winner gets a $20 iTunes voucher, your code MUST WORK to win. The challenge will be scored based on its:
- Scope: To what extent does the code implement the features specified in this document
- Correctness: To what extent is the code consistent with the specifications and free of bugs
- Design: To what extent is the code written well (clearly, efficiently and logically)
- Style: To what extent is the code readable (commented, variables named logically)

There will be other prizes so please at least attempt it!

Found a problem (or a spelling error, there will be many)? Summit a pull request or tell me on the groups!

Happy coding!