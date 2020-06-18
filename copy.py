def copy(l1,l2=[]):
	if l1==[]:
		return l2
	else:
		print(type(l2))
		l2.append(l1[0])
		copy(l1[1:],l2)
	return l2
def main():
	l1=eval(input('Enter the list: '))
	print(copy(l1))

if __name__=='__main__':
	main()				