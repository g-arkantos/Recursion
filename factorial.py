def factorial(n):
	#assert n>=1
	if n==0 or n==1:
		return 1
	else:	
		return n*factorial(n-1)
	 

m=int(input("Enter a number: "))	
fact=factorial(m)	
print(fact)