for _ in range(int(input())):
	n=int(input())
	l=list(map(int,input().split()))
	li=sorted(l)
	c=0
	mi=li[0]
	for i in range(n):
		if l[i]%mi!=0 and l[i]!=li[i]:
			c=1
			break
	if c==0:
		print("YES")
	else:
		print("NO")
