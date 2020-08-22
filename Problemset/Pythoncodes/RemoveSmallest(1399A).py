for _ in range(int(input())):
	n=int(input())
	l=list(map(int,input().split()))
	ans=0
	l.sort()
	for i in range(1,n):
		if l[i]-l[i-1]>1:
			ans=1
			break
	if ans==1:
		print("NO")
	else:
		print("YES")
