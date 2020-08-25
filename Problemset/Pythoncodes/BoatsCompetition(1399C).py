for _ in range(int(input())):
	n=int(input())
	temp=list(map(int,input().split()))
	l=[0]*(n+1)
	for i in temp:
		l[i]+=1
	ans=0
	for s in range(2,(2*n)+1):
		cur=0
		for i in range(1,(s+1)//2):
			if s-i<=n:
				cur+=min(l[i],l[s-i])
		if s%2==0:
			cur+=l[s//2]//2
		ans=max(ans,cur)
	print(ans)
