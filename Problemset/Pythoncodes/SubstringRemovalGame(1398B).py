for _ in range(int(input())):
	s=input()
	n=len(s)
	l=[]
	c=0
	for i in range(n):
		if s[i]=="1":
			c+=1
		else:
			if c!=0:
				l.append(c)
			c=0
	if c!=0:
		l.append(c)
	l.sort(reverse=True)
	ans=0
	n=len(l)
	for i in range(0,n,2):
		ans+=l[i]
	print(ans)
