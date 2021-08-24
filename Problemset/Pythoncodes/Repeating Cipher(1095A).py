n=int(input())
s=input()
ans=''
i=0
j=1
while i<n:
	ans=ans+s[i]
	i=i+j
	j+=1
print(ans)
