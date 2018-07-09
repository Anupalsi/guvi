n=int(input())
list1=[]
for i in range(n):
	lst=list(input().split())
	list1.append(lst)
m=int(input())
list2=[]
for i in range(m):
	lst=input()
	list2.append(lst)
for i in list2:
	list3=[]
	for j in range(n):
		for k in list1[j]:
			if i==k:
				list3.append(j+1)
	if len(list3)==0:
		print("-1")
	else:
		stri=""
		for i in list3:
			stri=stri+str(i)+" "
		print(stri.strip())
