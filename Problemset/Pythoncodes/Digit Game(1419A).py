for _ in range(int(input())):
	n=int(input())
	s=input()
	if n%2==0:
		ans=1
		for i in range(1,n,2):
			if int(s[i])%2==0:
				ans=2
				break
	else:
		ans=2
		for i in range(0,n,2):
			if int(s[i])%2!=0:
				ans=1
				break
	print(ans)
