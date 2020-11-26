for _ in range(int(input())):
	n=int(input())
	l=list(map(int,input().split()))
	temp=[l[0]]
	nn=0
	for i in range(1,n):
		if l[i]!=temp[nn]:
			nn+=1
			temp.append(l[i])
	d={}
	for i in temp:
		d[i]=d.get(i,0)+1
	nn+=1
	mi=-1
	ans=-1
	for i in temp:
		if ans==-1:
			mi=i
			ans=d[i]+1
		else:
			if ans>d[i]+1:
				mi=i
				ans=d[i]+1
	ans=min(ans,d[temp[0]],d[temp[nn-1]])
	if temp[0]==temp[nn-1]:
		ans=min(ans,d[temp[0]]-1)
	print(ans)
