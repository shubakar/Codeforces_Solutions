for _ in range(int(input())):
	n=int(input())
	l=list(map(int,input().split()))
	low=0
	h=n-1
	while low<=h:
		print(l[low],end=" ")
		if low!=h:
			print(l[h],end=" ")
		low+=1
		h-=1
	print()
