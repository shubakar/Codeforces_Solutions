for _ in range(int(input())):
	n=int(input())
	l=list(map(int,input().split()))
	l=l[::-1]
	for i in l:
		print(i,end=" ")
	print()
