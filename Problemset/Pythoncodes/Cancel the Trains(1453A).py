for _ in range(int(input())):
	n,m=map(int,input().split())
	l=list(map(int,input().split()))
	r=list(map(int,input().split()))
	i=0
	j=0
	ans=0
	while i<n and j<m:
		if l[i]==r[j]:
			ans+=1
			i+=1
			j+=1
		elif l[i]<r[j]:
			i+=1
		elif l[i]>r[j]:
			j+=1
	print(ans)
