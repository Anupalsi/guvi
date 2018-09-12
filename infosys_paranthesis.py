st=raw_input()
a=list(st)
print(a)
#a=["(","(",")","(",")",")"]
b=[]
count=0
c=[]
u=100
for i in range(len(a)):
 
	if a[i]=="(":
		count=count+1
		if count!=u:
			b.append(count)
		c.append(count)
	if a[i]==")" and len(b)==0:
		u=count+1
		c.append(u)
 
	elif a[i]==")":
		c.append(b.pop())
	else:
		k=0
print(c)
 
