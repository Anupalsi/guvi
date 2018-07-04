
n=[11,2,3,14,34,67,24,56]
x=14
m=[]
for i in n:
 	if i<=x:
 		m.append(x-i)
 	else:
 		m.append(i-x)
m.sort()
list2=[]
c=m.count(0)
for i in range(3+c):
	e=m[i]
	for j in n:
		if j<=x:
			g=x-j
		else:
			g=j-x
		if e==g:
			u=list2.count(j)
			if u==0:
				list2.append(j)
				break
sum=0
for i in list2:
	if i!=x:
		sum=sum+i
print(sum)
	
