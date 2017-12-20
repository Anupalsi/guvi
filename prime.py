num=17
x=0
flag=0
for i in range(2,num):
	if(num%i==0):
		flag=1
		print("not prime no")
		break
if(flag!=1):
	print("prime no")
