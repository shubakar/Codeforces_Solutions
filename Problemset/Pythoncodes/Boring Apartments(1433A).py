for _ in range(int(input())):
	n=input()
	t=int(n[0])
	ans=10*(t-1)
	t=len(n)
	for i in range(1,t+1):
		ans+=i
	print(ans)
