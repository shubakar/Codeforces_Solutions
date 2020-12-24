for _ in range(int(input())):
	n=int(input())
	l=list(map(int,input().split()))
	d={}
	c=0
	for i in l:
		d[i]=d.get(i,0)
		if d[i]!=0:
			c=1
			break
		d[i]=1
	if c==0:
		print("NO")
	else:
		print("YES")
