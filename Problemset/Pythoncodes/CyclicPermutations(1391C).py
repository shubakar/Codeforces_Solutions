n=int(input())
fact=1
res=1
mod=10**9+7
for i in range(1,n+1):
	fact=(fact*i)%mod
	if i>=2:
		res=(res*2)%mod
ans=fact-res
if ans<0:
	ans+=mod
print(ans)
