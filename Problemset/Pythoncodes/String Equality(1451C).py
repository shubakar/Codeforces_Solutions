def fu(A,B,n,k):
	temp=[0]*26
	t=ord("a")
	for i in range(n):
		temp[ord(A[i])-t]-=1
		temp[ord(B[i])-t]+=1
	cu=0
	for i in range(26):
		if temp[i]==0:
			continue
		else:
			if abs(temp[i])%k!=0:
				print("NO")
				return
			if temp[i]>0:
				if cu<temp[i]:
					print("NO")
					return
				else:
					cu-=temp[i]
			else:
				cu+=abs(temp[i])
	print("YES")
				
for _ in range(int(input())):
	n,k=map(int,input().split())
	a=input()
	b=input()
	fu(a,b,n,k
