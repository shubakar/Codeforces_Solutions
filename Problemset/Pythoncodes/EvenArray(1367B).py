for _ in range(int(input())):
	n=int(input())
	l=list(map(int,input().split()))
	e=0
	o=0
	for i in range(n):
		if i%2==0:
			if l[i]%2!=0:
				o+=1
		else:
			if l[i]%2==0:
				e+=1
	if o==e:
		print(o)
	else:
		print("-1")
