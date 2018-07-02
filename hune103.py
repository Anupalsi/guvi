n=int(input())
k=1
while n>0:
	f=""
	for i in range(k):
		if i==0:
			f="1"
		else:
			f=f+" "+"1"
	f.strip()
	print(f)
	k=k+2
	n=n-1
