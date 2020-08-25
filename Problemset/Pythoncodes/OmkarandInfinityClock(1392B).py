for _ in range(int(input())):
	n,k=input().split()
	n=int(n)
	k=int(k)
	l=list(map(int,input().split()))
	ma=max(l)
	if k%2==1:
		for i in range(n):
			print(ma-l[i],end=" ")
	else:
		for i in range(n):
			l[i]=ma-l[i]
		ma=max(l)
		for i in range(n):
			print(ma-l[i],end=" ")
	print()
