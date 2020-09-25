n=int(input())
l=list(map(int,input().split()))
for i in range(1,n):
	if i%2!=0:
		if l[i-1]<l[i]:
			l[i],l[i-1]=l[i-1],l[i]
	else:
		if l[i]<l[i-1]:
			l[i],l[i-1]=l[i-1],l[i]
if n%2==0:
	ans=(n//2)-1
else:
	ans=(n//2)
print(ans)
for i in range(n):
	print(l[i],end=" ")
