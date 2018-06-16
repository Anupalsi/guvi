from itertools import combinations
n=int(input())


list1=[]
for i in range(n):
	list1.append(i)
comb = combinations(list1,2)

list2=[]
for i in list(comb):
     
    list2.append(list(i))
k=len(list2)
print(k)
