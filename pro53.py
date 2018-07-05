# your code goes here
s=input()
k=s.replace(" ","")
k1=k.lower()
list1=list(k1)
list1.sort()
k2=set(list1)
length=len(k2)
if length==26 and k.isalpha:
	print("yes")
else:
	print("no")
