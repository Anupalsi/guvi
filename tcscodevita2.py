# your code goes here
a=int(input())
list1=[]
for i in range(2,a):
	flag1=0
	for j in range(2,i):
		if i%j==0:
			flag1=1
			break
	if flag1==0:
		list1.append(i)
#print(list1)
count=0
for i in range(2,len(list1)):
	sum=0
	for j in range(i):
		sum=sum+list1[j]
	if sum in list1:
		count=count+1
	if sum>a:
		break
print(count)
	
