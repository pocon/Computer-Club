# Evan Hockings
n = input('');  r = 'Prime'
if n < 2:   r = 'Not prime'
else: 
	for i in range(2,n): 
		if n % i == 0:  r = 'Not prime'
print r
