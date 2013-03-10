postfixlist=[] # This is the list that will hold the values and/or operators
exp=raw_input("Enter the postfix expression:")
for i in exp:
 if i=="+": # Pop off wo values when you get an operator
  tmp1=postfixlist.pop()
  tmp2=postfixlist.pop()
  postfixlist.append((tmp1+tmp2)%10) # Push the calculated value onto the list
 elif i=="*": # Pop off two values when you get an operator
  tmp1=postfixlist.pop()
  tmp2=postfixlist.pop()
  postfixlist.append((tmp1*tmp2)%10) # Push the calculated value onto the list
 else:
  postfixlist.append(int(i)) # If it's just a number, push it on the list. Note that this program doesn't provide sanity checking eg to check if the user entered a letter". Make sure that we're casting to int before adding numbers to the list.
print "The result is "+str(postfixlist[0]) # Remember to convert the int back to a string to print it
