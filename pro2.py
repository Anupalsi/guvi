# your code goes here
# your code goes here
#n=5
#k=2

#l=n-k
#431299 3
str=input()
a=str.split(" ")
n=len(a[0])
k=int(a[1])
l=n-k
list1=[]
for i in range(n):
	list1.append(a[0][i])
	
f=n-k
def chlm(z):

	letter=list1[z]
	for i in range(1,l):
		letter+=list1[z+1]
		
		z=z+1
	return(letter)
mi=chlm(0)
min=int(mi)
for i in range(1,f):
	mq=chlm(i)
	m=int(mq)
	if min>m:
		min=m
print(min)
# your code goes here
