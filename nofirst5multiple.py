n=input("enter the no \n")
sum=n-5
for i in range(0,5):
	if(n%5!=0):
		e=n%5
		g=5-e
		n=g+n
		sum=n-5
		sum=sum+5
		print(sum)
	else:
		sum=sum+5
		print(sum)
