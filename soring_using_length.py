n=int(input())
string=input()
list1=string.split()
for i in range(n):
	min=list1[i]
	for j in range(i+1,n):
		if list1[i]>list1[j] and len(list1[i])==len(list1[j]) or len(list1[i])>len(list1[j]):
			
			min,list1[j]=list1[j],min
	print(min,end=' ')
