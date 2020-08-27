for _ in range(int(input())):
	n=int(input())
	l=list(map(int,input().split()))
	if n==1:
		print("First")
		continue
	nxt=1
	for i in range(n-2,-1,-1):
		if nxt==1:
			if l[i]!=1:
				nxt=1
			else:
				nxt=2
		else:
			nxt=1
	if nxt==1:
		print("First")
	else:
		print("Second")
				
