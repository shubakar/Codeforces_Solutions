for _ in range(int(input())):
	n=int(input())
	l=list(map(int,input().split()))
	i=1
	j=0
	ans=0
	while i<n:
		if l[i]>=l[i-1]:
			i+=1
		else:
			j=i-1
			i+=1
			while i<n and l[i]<l[i-1]:
				i+=1
			ans+=(l[j]-l[i-1])
	print(ans)
