int1=input("Enter first integer ")
int2=input("Enter second integer ")
if (type(int1)==int and type(int2)==int):
 if int1<int2:
  print str(int1)+" is smaller than "+str(int2)
 elif int1>int2:
  print str(int1)+" is larger than "+str(int2)
 else:
  print str(int1)+" is equal to "+str(int2)
else:
 print "Please enter integers"
