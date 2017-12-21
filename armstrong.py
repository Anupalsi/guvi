# your code goes here
n=input()
temp=n
rev=0
while(n>0):
	r=n%10
	rev=rev+r*r*r
	n=n/10
if(temp==rev):
	print("yes")
else:
	print("no")
