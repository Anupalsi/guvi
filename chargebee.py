n=int(input())
stri=input()
list1=stri.split(",")
for i in range(n):
	list1[i]=int(list1[i])
list2=[]
for i in range(1,n):
	if  list1[i]/list1[i-1]==3 and list1[i]%list1[i-1]==0:
		list2.append(list1[i-1])
	elif list1[i-1]/list1[i-2]==3 and list1[i-1]%list1[i-2]==0:
		list2.append(list1[i-1])
 
	else:
		list2.append(0)
if  list1[n-1]/list1[n-2]==3 and list1[n-1]%list1[n-2]==0:
		list2.append(list1[n-1])
else:
	list2.append(0)
pos=0
list4=[]
while pos<(n-2):
	list3=[]
	if list2[pos]>0 and list2[pos+1]/list2[pos]==3:
		while list2[pos]>0 and list2[pos+1]/list2[pos]==3:
			list3.append(list2[pos])
			pos=pos+1
			if pos>=n-2:
				break
			#print(list3)
		if pos<n-2:
			if list2[pos-1]>0 and list1[pos]/list1[pos-1]==3:
				list3.append(list2[pos])
				pos=pos+1
	else:
		pos=pos+1
	if list3!=[]:
		list4.append(list3)
m=len(list4)
if list2[n-2]>0 and list2[n-2]/list2[n-3]==3:
	list4[m-1].append(list2[n-2])
	if list2[n-1]>0 and list2[n-1]/list2[n-2]==3:
		list4[m-1].append(list2[n-1])
elif list2[n-2]>0 and list2[n-1]>0:
	if list2[n-1]/list2[n-2]==3:
		list4.append([list2[n-2],list2[n-1]])
list6=[]
for i in range(len(list4)):
	count=0
	for j in range(i,len(list4)):
		if list4[i]==list4[j]:
			count=count+1
	v=str(list4[i][0])
	for k in range(1,len(list4[i])):
		v=v+","+str(list4[i][k])
	if v not in list6:
		print("SEG:"+v+" "+"OCCURANCE:"+str(count))
	list6.append(v)
