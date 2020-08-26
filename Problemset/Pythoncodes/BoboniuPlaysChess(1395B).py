def fu(a,b,d,x):
	for i in range(a,b,d):
		print(x,i)
n,m,x,y=input().split()
n=int(n)
m=int(m)
x=int(x)
y=int(y)
for i in range(y,m+1):
	print(x,i)
for i in range(y-1,0,-1):
	print(x,i)
c=0
for i in range(x+1,n+1):
	if c==0:
		fu(1,m+1,1,i)
		c=1
	else:
		fu(m,0,-1,i)
		c=0
for i in range(1,x):
	if c==0:
		fu(1,m+1,1,i)
		c=1
	else:
		fu(m,0,-1,i)
		c=0
