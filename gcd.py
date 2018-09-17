string=input()
a=string.split()
for i in range(2):
	a[i]=int(a[i])
gcd=1
for i in range(1,min(a)+1):
	
	if a[0]%i==0 and a[1]%i==0:
		gcd=i
print(gcd)
