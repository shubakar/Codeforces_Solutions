for _ in range(int(input())):
	n=int(input())
	if n<31:
		print("NO")
		continue
	print("YES")
	if n==36:
		print("1 6 14 15")
	elif n==40:
		print("5 6 14 15")
	elif n==44:
		print("6 7 10 21")
	else:
		print("6 10 14",n-30)
