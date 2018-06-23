from itertools import combinations
l=input()
m=list(l)
list1=[]
for i in range(2,len(m)+1):
	comb=combinations(m,i)
	for i in list(comb):
		list1.append(list(i))
list3=[]
for j in range(len(list1)):
	list2=[]
	m=len(list1[j])
	for i in range(m-1,-1,-1):
		list2.append(list1[j][i])
	list3.append(list2)
flag=0
for i in range(0,len(list1)):
	if list1[i]==list3[i]:
		flag=len(list1[i])
i=len(l)
print(i-flag)
	
