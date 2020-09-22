for _ in range(int(input())):
	n=int(input())
	l=[0]*257
	for i in range(n):
		a=input()
		for i in a:
			l[ord(i)]+=1
	ans=1
	for i in range(257):
		if l[i]%n!=0:
			ans=0
			break
	if ans==1:
		print("YES")
	else:
		print("NO")
			
