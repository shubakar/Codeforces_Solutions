for _ in range(int(input())):
	ans=0
	n=int(input())
	while (ans*(ans+1))//2<n:
		ans+=1
	if (ans*(ans+1))//2==1+n:
		ans+=1
	print(ans)
