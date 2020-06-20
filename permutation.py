def permutation(list1,list2=[],k=0,pos=0):
	list2.insert(pos,list1[k])
	if len(list1)==len(list2):
		print(list2)
	else:
		permutation(list1,list2,k+1,0)
	list2.remove(list1[k])
	if pos<k:		
		permutation(list1,list2,k,pos+1)
def main():
	lst=list(eval(input('Enter the contents to the list: ')))
	permutation(lst)
if __name__=='__main__':
	main()