Week 2 Exercises
=================

TBA

### Challenge - Indefinitely Nested Lists ###

Note 1: We've put this up early in case experienced people want to have a crack at it, everyone else shouldn't worry too much because you'll learn more useful stuff that you MIGHT need (we haven't done it yet either) this coming Tuesday.

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

[[4,[3,1],2],8,[3,4,[1,1]]] should be ordered to [8,[[1,1],3,4],[2,[1,3],4]] (index of [[1,1],3,4] is index of [1,1]+3+4=2+3+4=9, and index of [4,[3,1],2] is 4+index of [3,1]+2=4+4+2=10)

NB: we don't care about the order if two indices/sizes are the same, for example [[1,3],4] and [4,[1,3]] are both valid.

#### Scorer ####

A copy of the challenge scorer is available here: https://github.com/pocon/Computer-Club/blob/master/Utilities/score.py

#### Extension ####

TBA
