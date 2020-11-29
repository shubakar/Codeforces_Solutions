for _ in range(int(input())):
	n,m,r,c=input().split()
	n=int(n)
	m=int(m)
	r=int(r)
	c=int(c)
	print(max(r+c-2,n-r+c-1,r-1+m-c,n-r+m-c))
