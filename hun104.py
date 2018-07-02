n=input()
sum=0
for i in range(len(n)):
	for j in range(i+1):
		sum=sum+int(n[j])
print(sum)
