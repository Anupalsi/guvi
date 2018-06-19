# your code goes here
stri=input()
li=stri.split(" ")
a=int(li[0])
b=int(li[1])
c=int(li[2])
sum=0
temp=a
while(a>=(2*(c+b))):
    sum=2*(c+b)+sum
    a=a-2*(c+b)
if sum==temp:
    print("YES")
else:
    summm=sum
    aaa=a
    while a>=(2*b):
        sum=sum+2*b
        a=a-(2*b)
    flag=0
    if sum==temp:
        flag=1
    while aaa>=(2*c):
        summm=summm+2*c
        aaa=aaa-2*c
    if summm==temp:
        flag=2
    if flag==1 or flag==2:
        print("YES")
    else:
        print("NO")
	
		
			
			
			
			
			
			
			
			
