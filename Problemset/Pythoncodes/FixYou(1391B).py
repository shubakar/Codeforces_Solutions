for _ in range(int(input())):
	n,m=input().split()
	n=int(n)
	m=int(m)
	l=[]
	for i in range(n):
		l.append(input())
	ans=0
	for i in range(n):
		if l[i][m-1]!="D":
			ans+=1
	for i in range(m):
		if l[n-1][i]!="R":
			ans+=1
	print(ans-2)
