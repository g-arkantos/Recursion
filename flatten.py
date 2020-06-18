def flatten(l1, l2=[]):
	for element in l1:
		if type(element)!=list:
			l2.append(element)
		else:
			flatten(element)
	return l2
def main():
	list1=eval(input("Enter the list: "))
	print(flatten(list1))	
if __name__=='__main__':
	main()				