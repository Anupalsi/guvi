N=int(input())
a=input()
b=input()
aa=a.split(" ")
bb=b.split(" ")
list=[]
for i in range(N):
    for j in range(N):
        if aa[i]==bb[j]:
            list.append(aa[j])
s=" ".join(list)
print(s)
