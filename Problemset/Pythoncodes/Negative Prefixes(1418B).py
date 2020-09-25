for _ in range(int(input())):
	n=int(input())
	a=list(map(int,input().split()))
	l=list(map(int,input().split()))
	temp=[]
	for i in range(n):
		if l[i]==0:
			temp.append(a[i])
	temp.sort(reverse=True)
	i=0
	j=0
	k=0
	while k<n:
		if l[k]==1:
			print(a[k],end=" ")
		else:
			print(temp[j],end=' ')
			j+=1
		k+=1
	print()
