import math
for _ in range(int(input())):
	n,m=input().split()
	n=int(n)
	m=int(m)
	ans=math.floor(((n*m)+1)/2)
	print(ans)
	
