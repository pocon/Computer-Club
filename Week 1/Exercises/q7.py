# Without using booleans or conditionals

num=input("Enter the number to be tested ")
string=str(num)
num2=""
c=0
while c<len(string):
 num2+=string[len(string)-c-1]
 c+=1
print num-int(num2)

#If the number is palindromic, the output is 0

# Two Liner:

num = raw_input("Enter The Number To Be Tested: ")
print num[::-1] == num
