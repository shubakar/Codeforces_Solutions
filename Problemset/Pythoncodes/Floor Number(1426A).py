import math
for _ in range(int(input())):
	n,x=input().split()
	n=int(n)
	x=int(x)
	if n<=2:
		print(1)
	else:
		n-=2
		ans=math.floor(n/x)
		if ans*x<n:
			ans+=1
		ans+=1
		print(ans)
	
