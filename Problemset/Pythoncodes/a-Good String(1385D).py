def fu(l,start,end,e):
	if start>end:
		return 0
	if start==end:
		if l[start]==e:
			return 0
		else:
			return 1
	mid=(end+start)//2
	left=fu(l,start,mid,e+1)
	right=fu(l,mid+1,end,e+1)
	return min(left+((end-start)//2)-l[mid+1:end+1].count(e) , right+((end-start)//2)-l[start:mid+1].count(e))+1
for i in range(int(input())):
	n=int(input())
	s=input()
	l=[]
	for i in s:
		l.append(ord(i)-ord("a")+1)
	print(fu(l,0,n-1,1))
