def power():
    
    inp=input()
    a=inp.split(" ")
    N=int(a[0])
    K=int(a[1])
    if K==1:
        return(N==1)
    else:
        pow=1
        while pow<N:
            pow=pow*K
        return(pow==N)
m=power()
if(m==True):
	print("yes")
else:
	print("no")
