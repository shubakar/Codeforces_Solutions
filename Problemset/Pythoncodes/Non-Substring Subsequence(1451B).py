def fu(A,n,m,l):
	ans=False
	for i in range(0,n):
		if A[i]==A[n]:
			return True
	for i in range(m+1,l):
		if A[m]==A[i]:
			return True
	return False
for _ in range(int(input())):
	n,q=map(int,input().split())
	s=input()
	for i in range(q):
		w,m=map(int,input().split())
		t=fu(s,w-1,m-1,n)
		if t:
			print("YES")
		else:
			print("NO"
