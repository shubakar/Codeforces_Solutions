for _ in range(int(input())):
	n,x=input().split()
	n=int(n)
	x=int(x)
	l=list(map(int,input().split()))
	countx=0
	netsum=0
	for i in l:
		if i==x:
			countx+=1
		netsum+=x-i
	if countx==n:
		print(0)
	elif netsum==0 or countx!=0:
		print(1)
	else:
		print(2)
