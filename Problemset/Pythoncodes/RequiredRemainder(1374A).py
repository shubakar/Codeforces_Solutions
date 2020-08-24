for _ in range(int(input())):
	x,y,n=input().split()
	x=int(x)
	y=int(y)
	n=int(n)
	temp=n//x
	if temp*x+y<=n:
		print(temp*x+y)
	else:
		if temp==0:
			print(y)
		else:
			print((temp-1)*x+y)
