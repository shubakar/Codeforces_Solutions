for _ in range(int(input())):
	n=int(input())
	l=list(map(int,input().split()))
	c=0
	for i in range(1,n-1):
		if l[i-1]<l[i] and l[i]>l[i+1]:
			print("YES")
			print(i,i+1,i+2)
			c=1
			break
	if c==0:
		print("NO")
