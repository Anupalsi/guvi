num=int(raw_input("Enter a number\n"))
sum1=0
n=num
while num!=0:
	rem=num%10
	sum1=sum1*10+rem
	num=num/10
if sum1==n:
	print("palindrome")
else:
	print("not palindrome")
