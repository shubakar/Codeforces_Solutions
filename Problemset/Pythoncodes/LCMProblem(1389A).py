for _ in range(int(input())):
	n,m=input().split()
	n=int(n)
	m=int(m)
	if 2*n<=m:
		print(n,2*n)
	else:
		print("-1 -1")
