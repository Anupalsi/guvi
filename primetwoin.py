a=input("enter lower limit")
b=input("enter higher limt")
flag=0
for i in range(a,b):
	for j in range(2,i):
		if(i%j == 0):
			break
	else:
		print(i)
