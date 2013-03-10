#mokhaccino 
n = input("Type in a Number to see if it is Prime ")
while True: 
	for i in range(2,n):
		if n%i ==0:
			exit("composite")
	else:	 
		exit("prime")