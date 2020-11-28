for _ in range(int(input())):
	n=int(input())
	l=list(map(int,input().split()))
	flag=0
	t=l[0]
	for i in range(1,n):
		if l[i]!=t:
			tt=i
			flag=1
			break
	if flag==0:
		print("NO")
	else:
		t=l[0]
		tt=-1
		print("YES")
		for i in range(1,n):
			if l[i]!=t:
				tt=i
				print(1,i+1)
		for i in range(1,n):
			if l[i]==t:
				print(tt+1,i+1)
