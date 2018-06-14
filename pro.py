# your code goes here
# your code goes here# your code goes here
n=int(input())
list1=[]
for i in range(n):
	app=input()
	list1.append(app)
min=len(list1[0])
for i in range(1,n):
	p=len(list1[i])
	if min>p:
		min=p
list2=[]
for i in range(min):
	letter=list1[0][i]
	flag=0
	for j in range(1,n):
		if letter!=list1[j][i]:
			flag=1
	if flag==0:
		list2.append(letter)
	else:
		break
a="".join(list2)
print(a)
