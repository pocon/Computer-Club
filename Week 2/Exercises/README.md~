Week 2 Exercises
=================

1. Write a program that takes in 2 integers and prints their quotient rounded to the nearest integer. ie 3/4 = 1, 8/5 = 2.
2. Write a program that accepts an integer and prints either that integer's floor or ceiling (floor means the integer part of the number (25.678543 -> 25) whilst ceiling is just the floor + 1) depending on user input (ie if the user types in "ceiling", you return the ceiling, etc)
3. Write a program that accepts a mathematical expression (addition and multiplication mod 10 only) using single digit numbers only in postfix notation as a string and computes the result. An example of a postfix expression is 23+5*8+. In postfix notation, as numerical values are read from the expression from left to right, they are appended to a list (originally empty). When an operator (ie + or *) is read, two values are popped off the list, the operation performed on them and the result appended to the list. In this case, our addition and multiplication operators are modulo 10 (ie use the % notation) so all your intermediate values and final answer should be single digit.
4. Write a program that accepts 2 integers and returns whether one is greater than the other (print this nicely) or they are equal. In addition, if non-integers are submitted, your program should fail NICELY.
5. Write a program that implements a very simple (and extremely insecure) password database using a dictionary (that you create). This should be of the form {username:password,username:password...} etc. Upon starting, it should ask for the username; if that username does not exist, it should nicely inform the user of that, if it does, it should then ask for the password. If this is incorrect, it should nicely inform the user of that, otherwise it should display a welcome message and then exit. Note: if you ever do write an actual password database thingy program, please don't use this method. Learn about cryptographic hash functions and salting and then write that program ;).
6. Write a function that accepts the two shorter side lengths of a right-angled triangle as arguments and returns the length of the hypotenuse using Pythagoras' Theorem. You could also write a program that actually makes use of this function.
7. Write a recursive function that takes n as an argument and prints the nth Fibonnaci number. A recursive function is one that contains a call to itself. For example:

def recurse():
 Random stuff goes here
 recurse()

Please ensure that your function will terminate eventually; if you do get yourself into a recursive infinite loop, you can use Ctrl-C to kill the program (or python will kill it itself once it exceeds its maximum recursion depth (which basically means how many times it can call itself))

More exercises will come soon, to enable you to practice slicing and sys.argv...

### Challenge - Indefinitely Nested Lists ###

Note 2: This challenge is possibly a little too difficult/abstract for week 2, if you can't do it don't freak out.

Let's call a list an "Indefinitely Nested List" if all its elements are either integers or Indefinitely Nested Lists.

Some examples of "indefinitely nested lists" that should make the concept clearer:

[3,4,2]

^ This is an example of a list of integers.

[[1,4],[4,-6,90]]

^ This is an example of a list of lists of integers.

[4,7,[8,1],[3,6,4]]

^ This is an example of a list of integers and lists of integers.

[[6,8,[3,56],[5,3]],[5,6],85,62,[-32,[4,-7]]]

^ This is an example of a list of integers and lists of integers and lists of integers.

Define the "index" of an Indefinitely Nested List as the sum of all integers in it plus the sum of all indices of Indefinitely Nested Lists in it.

For example, if I wanted the index of:

[3,4,2] I simply sum the elements, giving 9

[5,9,[3,4,2]] I sum the integer elements (5 and 9) and the indices of the indefinitely nested lists (i.e. the index of [3,4,2]). So I get 5+9+9 = 23.

For no apparent reason Patrick O'Connell has an "indefinitely nested list" lying around, as all cool kids do. He also coincidentally likes ordering things. Write as short a program as possible that takes in an "indefinitely nested list" and orders all elements and sub-elements according to size/index and then prints the ordered list.

That is, [3,4,2] should be ordered to [2,3,4] (i.e. in order of size)

[10,8,[3,4,2]] should be ordered to [8,[3,4,2],10] (index of [3,4,2] is 9, so it goes "between" 8 and 10 in size)

[[4,[3,1],2],8,[3,4,[1,1]]] should be ordered to [8,[[1,1],3,4],[2,[1,3],4]] (index of [[1,1],3,4] index of [1,1]+3+4=2+3+4=9, and index of [4,[3,1],2] is 4+index of [3,1]+2=4+4+2=10)

NB: we don't care about the order if two indices/sizes are the same, for example [[1,3],4] and [4,[1,3]] are both valid.

#### Scorer ####

A copy of the challenge scorer is available here: https://github.com/pocon/Computer-Club/blob/master/Utilities/score.py

#### Extension ####

TBA
