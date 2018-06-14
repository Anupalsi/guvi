N=int(raw_input())
a=raw_input()
b=raw_input()
aa=a.split(" ")
bb=b.split(" ")
l=[]
for i in range(N):
    for j in range(N):
        if aa[i]==bb[j]:
            l.append(aa[i])
a=set(l)
b=list(a)
b=" ".join(b)
print(b)
