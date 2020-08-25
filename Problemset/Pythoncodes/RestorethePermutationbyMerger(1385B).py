for _ in range(int(input())):
	n=int(input())
	l=list(map(int,input().split()))
	for i in range(2*n):
		if l[abs(l[i])-1]>0:
			print(abs(l[i]),end=" ")
			l[abs(l[i])-1]*=-1
	print()
