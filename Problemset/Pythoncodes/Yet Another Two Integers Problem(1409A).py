for _ in range(int(input())):
	a,b=input().split()
	a=int(a)
	b=int(b)
	ans=abs(a//10-b//10)
	if a>b and a%10>b%10:
		ans+=1
	elif a<b and a%10<b%10:
		ans+=1
	print(ans)
