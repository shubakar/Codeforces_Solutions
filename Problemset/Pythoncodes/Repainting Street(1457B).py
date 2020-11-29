def fu(A,n,k,x):
	ans=0
	i=0
	while i<n:
		if A[i]!=x:
			ans+=1
			i+=k
		else:
			i+=1
	return ans
for _ in range(int(input())):
	n,k=input().split()
	n=int(n)
	k=int(k)
	l=list(map(int,input().split()))
	d=[0]*101
	for i in l:
		d[i]=1
	ans=1000000000000
	for i in range(1,101):
		if d[i]==1:
			t=fu(l,n,k,i)
			ans=min(ans,t)
	print(ans)
