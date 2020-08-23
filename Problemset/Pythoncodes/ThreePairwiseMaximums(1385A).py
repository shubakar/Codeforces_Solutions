for _ in range(int(input())):
	x,y,z=input().split()
	x=int(x)
	y=int(y)
	z=int(z)
	if x!=y and x!=z and z!=y:
		print("NO")
		continue
	elif x==y and x==z and y==z:
		print("YES")
		print(x,x,x)
		continue
	else:
		ma=max(x,y,z)
		mi=min(x,y,z)
		mac=0
		if x==ma:
			mac+=1
		if y==ma:
			mac+=1
		if z==ma:
			mac+=1
		if mac!=2:
			print("NO")
			continue
		else:
			print("YES")
			print(mi,mi,ma)
