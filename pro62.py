stir=input()
n=len(stir)
list1=[]
for i in range(2,n+1):
	list1.append(stir[0:i])
print(list1)
list3=[]
for j in range(len(list1)):
	list2=[]
	m=len(list1[j])
	for i in range(m-1,-1,-1):
		list2.append(list1[j][i])
	
	a="".join(list2)
	list3.append(a)
print(list3)
flag=0
for i in range(0,len(list1)):
	if list1[i]==list3[i]:
		flag=i
if n==flag+2:
	print(0)
else:
	w=stir[flag+2:]
	print(len(w))
