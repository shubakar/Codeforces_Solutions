def fu(l):
	if l[8]>=1:
		print("Yes")
		return
	if sum(l[4:])>=2:
		print("YES")
		return
	if sum(l[6:])>=1:
		if sum(l[2:6])>=1:
			print("YES")
			return
	if l[4]==1 or l[5]==1:
		if sum(l[2:4])>=2:
			print("YES")
			return
	print("NO")
	return
n=int(input())
l=list(map(int,input().split()))
d={}
cou=[0]*9
for i in l:
	if d.get(i,0)!=0:
		if d[i]>=8:
			d[i]+=1
		else:
			cou[d[i]]-=1
			d[i]+=1
			cou[d[i]]+=1
	else:
		d[i]=1
		cou[1]+=1
q=int(input())
for i in range(q):
	temp=input().split()
	if temp[0]=="-":
		t=int(temp[1])
		d[t]=d.get(t,0)
		if d[t]<=8:
			cou[d[t]]-=1
			d[t]-=1
			cou[d[t]]+=1
		else:
			d[t]-=1
	else:
		t=int(temp[1])
		d[t]=d.get(t,0)
		if d[t]>=8:
			d[t]+=1
		else:
			cou[d[t]]-=1
			d[t]+=1
			cou[d[t]]+=1
	fu(cou)
