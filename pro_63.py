a=input()
b=list(a)
li=1
for i in range(1,len(b)):
	flag=0
	list4=b[:i]
	for j in range(0,len(list4)):
		if b[i]!=list4[j]:
			flag=flag+1
	if flag==len(list4):
		li=li+1
	else:
		break
print(li)
