from itertools import combinations
str=input()
a=str.split(" ")
n=len(a[0])
k=int(a[1])
l=n-k
list1=[]
for i in range(n):
	list1.append(int(a[0][i]))
comb = combinations(list1,l)

# Print the obtained combinations
list2=[]
for i in list(comb):
     
    list2.append(list(i))
list3=[]
for i in range(len(list2)):
	sum=0
	for j in range(l):
		sum=sum*10+int(list2[i][j])
	
	list3.append(sum)
m=min(list3)
print(m)
