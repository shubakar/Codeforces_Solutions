for _ in range(int(input())):
	n=int(input())
	s=input()
	if n<4:
		print("NO")
		continue
	if s[:4]=="2020":
		print("YES")
	elif s[n-4:]=="2020":
		print("YES")
	elif s[0]=="2" and s[n-1]=="0":
		if s[1]=="0" and s[2]=="2":
			print("YES")
		elif s[1]=="0" and s[n-2]=="2":
			print("YES")
		elif s[n-3]=="0" and s[n-2]=="2":
			print("YES")
		else:
			print("NO")
	else:
		print("NO")
