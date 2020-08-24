for _ in range(int(input())):
	s=input()
	c0=0
	c1=0
	for i in s:
		if i=="0":
			c0+=1
		else:
			c1+=1
	if min(c0,c1)%2==0:
		print("NET")
	else:
		print("DA")
