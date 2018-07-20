
import itertools
def design(n):
	sum=n
	if n>=2:
		for i in range(2,n):
			sum=sum+i
	print(sum) 
	if n>=3:
		for i in range(3,n):
			sum=sum+i
	print(sum)
		
design(5)			
