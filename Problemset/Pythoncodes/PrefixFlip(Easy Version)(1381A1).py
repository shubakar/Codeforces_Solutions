for _ in range(int(input())):
	n=int(input())
	a=input()
	b=input()
	k=0
	ans=[]
	for i in range(n):
		if a[i]!=b[i]:
			k+=1
			ans.append(i+1)
			if i-1>=0:
				k+=2
				ans.append(1)
				ans.append(i+1)
	print(k,end=" ")
	for i in ans:
		print(i,end=" ")
	print()
