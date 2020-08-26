for _ in range(int(input())):
	a0,a1,a2=input().split()
	b0,b1,b2=input().split()
	a0=int(a0)
	a1=int(a1)
	a2=int(a2)
	b0=int(b0)
	b1=int(b1)
	b2=int(b2)
	ans=0
	if a2>=b1:
		ans+=(b1*2)
		a2-=b1
		b1=0
	else:
		ans+=(a2*2)
		b1-=a2
		a2=0
	ans=ans-(min(max(b2-a2-a0,0),a1)*2)
	print(ans)
	
