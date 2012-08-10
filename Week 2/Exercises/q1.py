int1=input("First integer ")
int2=input("Second integer ")

if (float(int1)/int2-int1/int2)>=0.5:
 # We round up
 print int1/int2+1
else:
 # We round down
 print int1/int2
