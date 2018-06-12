n=int(input())
list=[]
for i in range(n):
    list.append(input())
min=len(list[0])
pos=0
for i in range(n):
    if min>len(list[i]):
        min=len(list[i])
        pos=i
    
print(list[pos])
