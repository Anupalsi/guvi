import itertools
def isposible(a,b,c,d):
	flag=0
	
	lst=[]
	p=max(c,d)
	for i in range(2,p+1):
		lst=lst+(list(map(list,(itertools.product([a,b], repeat=i)))))	
	for i in lst:
		if (i.count(a)>0 and i.count(b)>0):
			if c==sum(i):
				flag=1
				break
	for i in lst:
		if (i.count(a)>0 and i.count(b)>0):
			if d==sum(i):
				flag=flag+1
				break
	if (flag==2):
		print("posible")
	else:
		print("not")
isposible(1,2,3,4)
