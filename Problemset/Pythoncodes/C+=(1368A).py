for _ in range(int(input())):
	a,b,n=input().split()
	a=int(a)
	b=int(b)
	n=int(n)
	ma=max(a,b)
	mi=min(a,b)
	ans=0
	i=0
	while ma<=n and mi<=n:
		ans+=1
		if i==0:
			mi=mi+ma
			i=1
		else:
			ma=ma+mi
			i=0
	print(ans)
