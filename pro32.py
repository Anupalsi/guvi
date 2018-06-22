n=input()
m=n.split(" ")
row=int(m[0])
col=int(m[1])
a=[]
for i in range(row):
	q=input()
	k=q.split(" ")
	a.append(k)

a = sorted(a, key=lambda a_entry: a_entry[1]) 

for i in range(row):
	print(" ".join(a[i]))
