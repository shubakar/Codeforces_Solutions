for _ in range(int(input())):
	n=int(input())
	ans=0
	fla=0
	while n>1:
		if n%6==0:
			ans+=1
			n=n//6
		else:
			n=n*2
			if n%6==0:
				ans+=2
				n=n//6
			else:
				fla=1
				break
	if fla==1:
		print("-1")
	else:
		print(ans)
