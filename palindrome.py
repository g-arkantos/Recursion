'noon'
def palindrome(m):
	if m== '' :
		return True
	else: 	
		return m[0]==m[-1] and palindrome(m[1:-1])
	

def main():
	string=str(input('Enter a string: '))
	print(palindrome(string))

if __name__=='__main__':
	main()	