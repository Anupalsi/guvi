x=[]
y=[]
for i in range(3):
	a=input()
	b=a.split()
	x.append(int(b[0]))
	y.append(int(b[1]))
	
if ((y[1]-y[0]) * (x[2]-x[1])) == ((y[2]-y[1]) * (x[1]-x[0])) :
	print ('yes')
else :
	print('no')
