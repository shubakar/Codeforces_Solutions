for _ in range(int(input())):
	n=int(input())
	l=list(map(int,input().split()))
	s=0
	ans=0
	for i in l:
		s+=i
		if s<0:
			ans+=s
			s=0
	print(abs(ans))
