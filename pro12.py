b=input()
w=b.split(" ")
m=int(w[0])
n=int(w[1])
h=input()
list1=h.split(" ")
lee=[]
for i in range(n):
    g=input()
    lis=g.split(" ")
    lee.append(lis)

for i in range(n):
    k=int(lee[i][0])
    j=int(lee[i][1])
    sum=0
    for u in range(k-1,j):
        sum=sum+int(list1[u])
    print(sum)
        
    

    
