def multiply(a,b):
	c=0
	if b==0:
		return c
	else:
		c=(a+multiply(a,b-1))
		return c	
def main():
	a=int(input('Enter 1st number: '))	
	b=int(input('Enter 2nd number: '))
	print(multiply(a,b))

if __name__=='__main__':
	main()		