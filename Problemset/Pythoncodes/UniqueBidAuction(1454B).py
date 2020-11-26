for _ in range(int(input())):
	n=int(input())
	l=list(map(int,input().split()))
	d={}
	flag=0
	ans=-1
	a=-1
	for i in l:
		d[i]=d.get(i,0)+1
	for i in range(n):
		if d[l[i]]==1:
			flag=1
			if a==-1:
				a=l[i]
				ans=i+1
			else:
				if a>l[i]:
					a=l[i]
					ans=i+1
	print(ans)
