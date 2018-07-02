u=input()
list2=u.split()
m=input()
list1=m.split()
sum=0
for i in range(len(list1)):
	q=int(list1[i])
	if q<=int(list2[1]):
		sum=sum+1
print(sum)
