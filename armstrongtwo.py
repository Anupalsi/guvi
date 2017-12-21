a=input("lower limit\n")
b=input("upper limit\n")
for n in range(a,b):
	h=len(str(n))
	temp=n
	rev=0
	while(n>0):
		r=n%10
		rev=rev+r**h
		n=n/10
	if(temp==rev):
		print(temp)
