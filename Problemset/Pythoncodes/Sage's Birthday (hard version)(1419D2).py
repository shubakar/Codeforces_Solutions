n=int(input())
l=list(map(int,input().split()))
l.sort()
high=n//2
a=[]
low=0
temp=high
while low<temp:
	a.append(l[high])
	a.append(l[low])
	low+=1
	high+=1
while high<n:
	a.append(l[high])
	high+=1
ans=0
for i in range(1,n-1,2):
	if a[i]<a[i-1] and a[i]<a[i+1]:
		ans+=1
print(ans)
for i in a:
	print(i,end=" ")
