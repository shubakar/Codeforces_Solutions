for _ in range(int(input())):
	a,k=input().split()
	a=int(a)
	k=int(k)
	if a==k:
		print("0")
	elif k<a:
		if (a%2!=0 and k%2!=0) or (a%2==0 and k%2==0):
			print("0")
		else:
			print("1")
	else:
		print(k-a)
