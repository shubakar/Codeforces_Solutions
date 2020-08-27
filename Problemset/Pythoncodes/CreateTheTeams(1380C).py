import math
for _ in range(int(input())):
	n,x=input().split()
	n=int(n)
	x=int(x)
	l=list(map(int,input().split()))
	li=[0]*(n+1)
	for i in l:
		if x/i<=1:
			li[1]+=1
		else:
			if x/i>n:
				continue
			else:
				li[math.ceil(x/i)]+=1
	ans=0
	for i in range(1,n+1):
		ans+=li[i]//i
		if i<n:
			li[i+1]+=li[i]%i
	print(ans)
