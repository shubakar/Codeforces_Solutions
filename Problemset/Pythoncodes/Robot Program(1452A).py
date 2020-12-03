for _ in range(int(input())):
	x,y=map(int,input().split())
	ans=2*min(x,y)
	if x!=y:
		ans+=2*(abs(x-y)-1)+1
	print(ans)
