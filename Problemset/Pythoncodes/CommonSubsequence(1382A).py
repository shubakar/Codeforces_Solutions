for _ in range(int(input())):
	n,m=input().split()
	n=int(n)
	m=int(m)
	a=list(map(int,input().split()))
	b=list(map(int,input().split()))
	d={}
	for i in a:
		d[i]=1
	c=0
	for i in b:
		if d.get(i,None):
			print("YES")
			print("1",i)
			c=1
			break
	if c==0:
		print("NO")
