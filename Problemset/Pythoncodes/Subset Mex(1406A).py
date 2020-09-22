for _ in range(int(input())):
	n=int(input())
	l=list(map(int,input().split()))
	a=[0]*102
	for i in l:
		a[i]+=1
	ma1=-1
	ma2=-1
	for i in range(101):
		if a[i]>=2:
			if ma2==i-1:
				ma2=i
				ma1=i
			else:
				ma1=i
		elif a[i]==1:
			ma1=i
		else:
			break
	print(ma1+ma2+2)
	
