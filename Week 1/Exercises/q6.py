string=raw_input("Enter the string: ")
acc=""
c=0
while c<len(string):
 acc+=string[len(string)-c-1]
 c+=1
print acc

# One Line Solution Using the Fact that string[start:end:step] and a bit of hax:

print raw_input("Enter the String: ")[::-1]
