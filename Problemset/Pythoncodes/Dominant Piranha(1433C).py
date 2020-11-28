for i in range(int(input())):
	n=int(input())
	l=list(map(int,input().split()))
	ma=max(l)
	flag=0
	for i in range(n):
		if l[i]==ma:
			if i>0 and l[i-1]!=ma:
				flag=1
				print(i+1)
				break
			elif i<n-1 and l[i+1]!=ma:
				print(i+1)
				flag=1
				break
	if flag==0:
		print(-1)
