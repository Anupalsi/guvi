N=int(input())
def b(m):
    l="{0:b}".format(m)
    return int(l)
h=int(input("ënter the first no"))
if N==1:
    print(h)
else:    
 p=b(h)
 if N<3:
    m=int(input("ënter the 2 no"))
    u=b(m)
    p=p&u
 else:
    for i in range(2,N+1):
        me=int(input("enter the"+str(i)+"no"))
        u=b(me)
        p=p&u
 decimal = int(str(p), 2);
 print(decimal)
