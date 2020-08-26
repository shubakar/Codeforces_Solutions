for _ in range(int(input())):
	s=input()
	x=int(input())
	n=len(s)
	ans=[1]*n
	for i in range(n):
		if s[i]=="0":
			if i>=x:
				ans[i-x]=0
			if i+x<n:
				ans[i+x]=0
	c=0
	for i in range(n):
		if s[i]=="1":
			if (i>=x and ans[i-x]==1) or (i+x<n and ans[i+x]==1):
				continue
			else:
				c=1
				break
		else:
			if i>=x and ans[i-x]==1:
				c=1
				break
			if i+x<n and ans[i+x]==1:
				c=1
				break
	if c==0:
		for i in ans:
			print(i,end="")
	else:
		print(-1,end="")
	print()
	
