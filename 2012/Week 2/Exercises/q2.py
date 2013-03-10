num=input("Enter the number to be floored or ceilinged: ")
which=raw_input("Do you want the floor or ceiling? ")
if which=="floor":
 print int(num) # as int() automagically chops off the decimal part, giving the floor
elif which=="ceiling":
 print int(num)+1
else:
 print "Please enter floor or ceiling. Exiting..." # Just some basic sanity checking
