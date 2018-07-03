n=input()
q=list(n)
j=0
while (q[j]=="0"):
	del q[j]
i=-1
while (q[i]=="0"):
	del q[i]
m=q[:]
q.reverse()
if m==q:
	print("yes")
else:
	print("no")
