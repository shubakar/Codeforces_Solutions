for _ in range(int(input())):
	n=int(input())
	l=list(map(int,input().split()))
	pre="b"*l[0]
	alpha="c"
	prelen=l[0]
	for i in range(n):
		if l[i]==0:
			if prelen!=0:
				print(pre)
				if pre[0]=="b":
					pre="c"
					alpha="b"
				else:
					pre="b"
					alpha="c"
				prelen=1
				#print(pre)
			else:
				print("c")
				pre="b"
				prelen=1
		elif l[i]<=prelen:
			print(pre)
			if l[i]!=prelen:
				if pre[l[i]]=="b":
					alpha="c"
				else:
					alpha="b"
			pre=pre[:l[i]]
			prelen=l[i]
		else:
			temp=pre+alpha*(l[i]-prelen)
			print(temp)
			pre=temp
			prelen=l[i]
			if alpha=="b":
				alpha="c"
			else:
				alpha="b"
	print(pre)
