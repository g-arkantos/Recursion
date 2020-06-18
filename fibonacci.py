'1 1 2 3 5 8'

def fib(n):
	assert n>0
	if n==1:
		return 1
	elif n==2:
		return 1	
	else:
	 	return fib(n-1) + fib(n-2)

j=int(input('Enter a number: '))

fibonacci= fib(j)	
print(fibonacci) 		 