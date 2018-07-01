n=int(input())
sum=0
while n>9:
    l=list(str(n))
    su=1
    for i in range(len(l)-1):
        m=int(l[i])-int(l[i+1])
        if m==1 or m==-1:
            su=su+1
        if su==len(l):
            sum=sum+1
    n=n-1
if(n<=9):
    for i in range(n+1):
        sum=sum+1
print(sum)
