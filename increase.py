'''
a program that takes number n as an input parameter and prints n-digit strictly increasing numbers
'''
def increase(n,l=[]):
	if n==0:
		return 0
	elif n==1:
		return l.append(1)
	else:
		(increase(n-1))
		l.append(n)
		return l		
def main():
	num=int(input('Enter a number: '))
	print(increase(num))
if __name__=='__main__':
		main()	
