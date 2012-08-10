# Binary Basics

You currently know quite a bit about python, but you have not yet learnt the basics of how computers work with the code you write.

## What is binary
As you probably already know, computers run on electricity which is either on or off. Because computers can only work with 2 values an alphabet had to be developed for computers. That is binary, 1 or 0, true or false, on or off. Each 0 or 1 is called a bit.

## Counting in binary
How do you count in a number system that has only 0 and 1. Counting to 1 is easy but what about 2? We’ve run out of digits! To solve this we "carry the one", the same concept as in normal maths. This means we get 10 as two and 11 as three. Here are the numbers 0 to 4:
<table><tr><td>000</td></tr><tr><td>001</td></tr><tr><td>010</td></tr><tr><td>011</td></tr><tr><td>100</td></tr></table>
As we can see, counting up is quite easy. As in normal maths, we  can have as many zeros before the number as we want but in reality a computer is limited.

Now how do we convert numbers between binary and decimal form? Think of a decimal number such as 321. There are 3 numbers in the hundreds column, 2 numbers in the tens and 1 number in the ones.
<table><tr><th>100's</th><th>10's</th><th>1's</th></tr><tr><td>3</td><td>2</td><td>1</td></tr></table>
The same pattern is followed in binary. Decimal is base 10, so each column is a power of 10. Binary is base 2, so each column is a power of 2. So 111 in binary is 1 ∗ 4 + 1 ∗ 2 + 1 ∗ 1 = 7.
<table><tr><th>128</th><th>64</th><th>32</th><th>16</th><th>8</th><th>4</th><th>2</th><th>1</th></tr><tr><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td> <td>1</td> <td>1</td></tr></table>

To make life simpler it was decided to lump all these bits into a group, and the byte (8 bits) was born! Now that you understand binary have a look at this XKCD comic (http://xkcd.com/953/)

## Letters
So far we have seen how binary can be used to write numbers, but how can it be used to represent letters? Simple, we use ASCII! ASCII is a standard for representing letters in binary and the table can be found here (http://www.asciitable.com/). However, you only really need to know that uppercase A is 65 and lowercase a is 97.
If you are given eight columns (one byte) you can represent all the numbers from 0 to 255. ASCII replaces some of these numbers with characters! So the letter A in binary is written as 01000001.
This is why characters and integers are interchangeable in python using methods such as `ord("a") == 97` and `chr(97) == "a"`. You will use these in the Caesar Cipher challenge so it is helpful to understand how they work.

## Positions
You may have come across a strange phenomenon in python already that is a result of binary. Positions in an array or list are indexed starting at zero. For example: `list = [bob, max, james, liam]` in this list the first word "bob" is in position 0 `list[0] == "bob"`. Why do computers do this? It's because starting at one would waste a whole binary number, 0.