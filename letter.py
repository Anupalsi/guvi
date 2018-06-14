# your code goes here
n=5
k=2
l=n-k
list1=["2","1","3"]
f=n-k
def chlm(z):
	letter=list[z]
	while k<0:
		letter+=list[z+1]
		k=k-1
		z=z+1
		print(letter)
		return(letter)
mi=chlm(0)
min=int(mi)
for i in range(l+1):
	mq=chlm(i)
	m=int(mq)
	if min>m:
		min=m
print(min)
# your code goes here
