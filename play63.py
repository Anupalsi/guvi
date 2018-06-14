N=int(input())
a=input()
b=input()
aa=a.split(" ")
bb=b.split(" ")
a=set(aa)
b=set(bb)
n=len(a)
m=len(b)
list=[]
for i in range(n):
    for j in range(m):
        if aa[i]==bb[j]:
            list.append(aa[j])
s=" ".join(list)
print(s)
