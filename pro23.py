import itertools
n=int(input())
lst = list(map(list,(itertools.product([0, 1], repeat=n))))
m=2**n
for i in range(m):
	stri=str(lst[i][0])
	for j in range(1,n):
		stri=stri+str(lst[i][j])
	print(stri)
	
	
