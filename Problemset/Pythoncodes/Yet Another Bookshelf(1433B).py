for _ in range(int(input())):
	n=int(input())
	l=list(map(int,input().split()))
	ans=0
	cur=0
	flag=0
	for i in range(n):
		if l[i]==1:
			if flag==1:
				ans+=cur
			flag=1
			cur=0
		else:
			cur+=1
	print(ans)
