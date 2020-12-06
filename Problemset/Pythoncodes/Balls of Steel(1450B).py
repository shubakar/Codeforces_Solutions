for _ in range(int(input())):
	n,k=map(int,input().split())
	l=[]
	for i in range(n):
		t=list(map(int,input().split()))
		l.append(t[:])
	ans=-1
	for i in range(n):
		t=0
		for j in range(n):
			if abs(l[i][0]-l[j][0])+abs(l[i][1]-l[j][1])>k:
				t=-1
				break
		if t==0:
			ans=0
			break
	if ans==0:
		print(1)
	else:
		print(-1)
