for _ in range(int(input())):
	n=int(input())
	a=list(map(int,input().split()))
	b=list(map(int,input().split()))
	ami=a[0]
	bmi=b[0]
	for i in range(n):
		ami=min(a[i],ami)
		bmi=min(b[i],bmi)
	ans=0
	for i in range(n):
		amove=a[i]-ami
		bmove=b[i]-bmi
		ans+=max(amove,bmove)
	print(ans)
