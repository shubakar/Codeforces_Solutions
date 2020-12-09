for _ in range(int(input())):
	n,c0,c1,h=map(int,input().split())
	s=input()
	ans=0
	if c0==c1:
		ans=n*c1
	elif c0>c1:
		if c1+h>=c0:
			for i in s:
				if i=="1":
					ans+=c1
				else:
					ans+=c0
		else:
			for i in s:
				if i=="0":
					ans+=c1+h
				else:
					ans+=c1
	else:
		if c0+h>=c1:
			for i in s:
				if i=="1":
					ans+=c1
				else:
					ans+=c0
		else:
			for i in s:
				if i=="1":
					ans+=c0+h
				else:
					ans+=c0
	print(ans)
