n=int(input())
string=input()

list1=string.split()
for i in range(len(list1)):
	list1[i]=int(list1[i])
k=int(input())
max=0
for i in range(0,n-k+1):
	for j in range(0,k):
		if max<list1[i+j]:
			max=list1[i+j]
	print(max,end=' ')
