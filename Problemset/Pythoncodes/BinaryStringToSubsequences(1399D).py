for _ in range(int(input())):
	n=int(input())
	s=input()
	ans=0
	ec=0
	oc=0
	l=[]
	e=[]
	o=[]
	c=0
	for i in s:
		if i=="0":
			if oc==0:
				ans+=1
				ec+=1
				c+=1
				e.append(c)
				l.append(c)
			else:
				oc-=1
				ec+=1
				temp=o.pop()
				e.append(temp)
				l.append(temp)
		else:
			if ec==0:
				oc+=1
				ans+=1
				c+=1
				o.append(c)
				l.append(c)
			else:
				oc+=1
				ec-=1
				temp=e.pop()
				o.append(temp)
				l.append(temp)
	print(ans)
	for i in l:
		print(i,end=" ")
	print()
