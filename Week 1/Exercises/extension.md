Extension problems
==================

## Note ##

These are aimed at those who already have programming/python experience
However anyone who's read and understood the week 1 material should be able to do them, after some time, effort and research.


## Questions ##

1. Implement the RSA asymmetric encryption algorithm (https://en.wikipedia.org/wiki/RSA_%28algorithm%29). It should accept the integers (from the article) p, q, e and m (we're assuming the message has been converted to an integer already), perform checks on their validity (e.g. are p and q prime?), display NICE errors if they're not valid, and output an integer corresponding to the ciphertext. NB: You're only expected to use the basic algorithm as described, not fancy versions using the Chinese remainder theorem. You might also want to implement the corresponding decryption algorithm.

2. Implement the Lucas-Lehmer algorithm for testing the primality of Mersenne numbers with odd prime exponent (https://en.wikipedia.org/wiki/Lucas%E2%80%93Lehmer_primality_test). It should accept the Mersenne number as input, output a nice error message if it isn't a Mersenne number and/or its exponent isn't an odd prime, and output whether it is a prime or composite.

3. Aliasing is when 2 different variable names refer to the same object in memory. This can occur with lists. For example, the following code:

list1=[1,2,3,4,5]
list2=list1
list2[1]=50
print list1

would output [1,50,3,4,5]. This is because list1 and list2 refer to the same list in actuality. Suggest a way by which I could "clone" a list, i.e. create another list with exactly the values as the first but unaliased with it. That is, modifying an element of list2 should not modify the elements of list1 too.

NB: This question will require some more knowledge, for example how objects are stored in memory.
