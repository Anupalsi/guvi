list1=[]
for i in range(4):
	m=input()
	n=m.split()
	list1=list1+n
m=set(list1)
if len(m)==2:
	print("yes")
else:
	print("no")
