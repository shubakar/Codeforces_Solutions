for _ in range(int(input())):
	ss=input()
	s=0
	l=0
	ans=0
	for i in ss:
		if i=="(":
			s+=1
		if i=="[":
			l+=1
		if i==")":
			if s>0:
				s-=1
				ans+=1
		if i=="]":
			if l>0:
				l-=1
				ans+=1
	print(ans)
