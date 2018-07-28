# your code goes here# your code goes here
a=input()
b=input()
c=input()
list1=a.split()
list1=list(map(int,list1))

list2=b.split()
list2=list(map(int,list2))

list3=c.split()
list3=list(map(int,list3))
min1=10000

for x in range(list1[0]):
	sum=0
	list2[x]=list2[x]+2*list1[1]
	
	for i in range(list1[0]):
		sum=sum+list2[x]*list3[x]
		
		
	list2[x]=list2[x]-2*list1[1]
	#print(min1)
	if min1>sum:
		min1=sum
		
for x in range(list1[0]):
	sum=0
	list2[x]=list2[x]-2*list1[1]
	for i in range(list1[0]):
		sum=sum+list2[x]*list3[x]
		print(sum)
	list2[x]=list2[x]+2*list1[1]
	if min1>sum:
		min1=sum
for x in range(list1[0]):
	sum=0
	list3[x]=list3[x]+2*list1[1]
	for i in range(list1[0]):
		sum=sum+list2[x]*list3[x]
	list3[x]=list3[x]-2*list1[1]
	if min1>sum:
		min1=sum

for x in range(list1[0]):
	sum=0
	list3[x]=list3[x]-2*list1[1]
	for i in range(list1[0]):
		sum=sum+list2[x]*list3[x]
	list3[x]=list3[x]+2*list1[1]
	if min1>sum:
		min1=sum		
print(min1)
