# Without using booleans or conditionals

num=input("Enter the number to be tested ")
string=str(num)
num2=""
c=0
while c<len(string):
 num2+=string[len(string)-c-1]
 c+=1
print num-int(num2)

#Iff the number is palindromic, the output is 0
