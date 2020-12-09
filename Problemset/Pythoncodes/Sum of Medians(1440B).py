import math
# your code goes here
for _ in range(int(input())):
	n,k=map(int,input().split())
	l=list(map(int,input().split()))
	ans=0
	if n%2==0:
		s=n//2
		t=s+1
		s=s+1
		n=n*k
		for i in range(k):
			ans+=l[n-s]
			#print(l[n-s],end=" ")
			s=s+t
	else:
		s=math.ceil(n/2)
		n=n*k
		t=s
		for i in range(k):
			ans+=l[n-s]
			#print(l[n-s],end=" ")
			s=s+t
	print(ans)
