list1=[]
for i in range(3):
	a=input()
	(b,c)=a.split()
	list1.extend([b,c])
	
flag=0
x=list1[0]
y=list1[1]
for i in range(2,len(list1),2):
	if x!=list1[i]:
		flag+=2
	if y!=list1[i+1]:
		flag+=1
		
if flag==4 and flag==2:
	print("no")
elif flag==4 or flag==2:
	print("yes")
else:
	print("no")
