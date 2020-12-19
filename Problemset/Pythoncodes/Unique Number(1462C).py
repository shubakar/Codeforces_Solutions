for _ in range(int(input())):
	x=int(input())
	i=9
	ans=[]
	while i>0 and x>0:
		if x>=i:
			ans.append(i)
			x-=i
		i-=1
	if x==0:
		ans=ans[::-1]
		for i in ans:
			print(i,end="")
		print()
	else:
		print(-1)
