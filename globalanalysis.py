# your code goes here
# your code goes here
word1=list(input())
word2=list(input())
if len(word1)==len(word2):
	count=0
	for i in range(len(word1)):
		if word1[i]==word2[i]:
			count=count+1
	output=len(word1)-count
elif(len(word1)<len(word2)):
	count=0
	list1=[]
	for i in range(len(word1)):
		for j in range(len(word2)):
			if word1[i]==word2[j]:
				list1.append(j)
				count=1
	max=min(list1)
				
	for i in range(list1.index(max),len(list1)):
		if max<list1[i]:
			count=count+1
			max=list1[i]
		
	output=len(word2)-count
else:
	count=0
	list1=[]
	for i in range(len(word2)):
		for j in range(len(word1)):
			if word2[i]==word1[j]:
				list1.append(j)
				count=1
	max=min(list1)
				
	for i in range(list1.index(max),len(list1)):
		if max<list1[i]:
			count=count+1
			max=list1[i]
		
	output=len(word1)-count
	
print(output)
