n=input()
for i in range(len(n)):
	if n[i]>='a' and n[i]<='z':
		print(n[i].upper(),end='')
	if n[i]>='A' and n[i]<='Z':
		print(n[i].lower(),end='')
