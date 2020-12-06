for _ in range(int(input())):
	n=int(input())
	s=input()
	ans=""
	for i in s:
		if i=="b":
			ans+="b"
	for i in s:
		if i!="b":
			ans+=i
	print(ans)
