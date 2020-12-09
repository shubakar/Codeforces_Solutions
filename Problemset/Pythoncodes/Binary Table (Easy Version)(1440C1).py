def fu1(A,i,j,kkk):
	o=0
	z=0
	ans=[]
	for k in range(i,i+2):
		for m in range(j,j+2):
			if A[k][m]=="0" and z<2:
				z+=1
				A[k][m]="1"
				ans.append([k+1,m+1])
			elif A[k][m]=="1":
				A[k][m]="0"
				ans.append([k+1,m+1])
	kkk.append(ans[:])
	fu2(A,i,j,kkk)
def fu2(A,i,j,kkk):
	o=0
	ans=[]
	for k in range(i,i+2):
		for m in range(j,j+2):
			if A[k][m]=="0":
				A[k][m]="1"
				ans.append([k+1,m+1])
			elif A[k][m]=="1" and o==0:
				o=1
				A[k][m]="0"
				ans.append([k+1,m+1])
	kkk.append(ans[:])
	fu3(A,i,j,kkk)
def fu3(A,i,j,kkk):
	ans=[]
	if A[i][j]=="1":
		ans.append([i+1,j+1])
		A[i][j]="0"
	if A[i+1][j]=="1":
		ans.append([i+2,j+1])
		A[i+1][j]="0"
	if A[i][j+1]=="1":
		ans.append([i+1,j+2])
		A[i][j+1]="0"
	if A[i+1][j+1]=="1":
		ans.append([i+2,j+2])
		A[i+1][j+1]="0"
	kkk.append(ans[:])
	return
def fu4(A,i,j,kkk):
	ans=[]
	ans.append([i+1,j+1])
	ans.append([i+1,j+2])
	ans.append([i+2,j+1])
	A[i][j]="0"
	A[i+1][j]="0"
	A[i][j+1]="0"
	kkk.append(ans[:])
	fu1(A,i,j,kkk)
def fu(A,i,j,ans):
	t=int(A[i][j])+int(A[i+1][j])+int(A[i][j+1])+int(A[i+1][j+1])
	if t==4:
		fu4(A,i,j,ans)
	elif t==3:
		fu3(A,i,j,ans)
	elif t==2:
		fu2(A,i,j,ans)
	elif t==1:
		fu1(A,i,j,ans)
for i in range(int(input())):
	n,m=map(int,input().split())
	l=[]
	for i in range(n):
		t=list(input())
		l.append(t[:])
	ans=[]
	for i in range(0,n-1):
		for j in range(0,m-1):
			fu(l,i,j,ans)
	print(len(ans))
	for i in ans:
		for j in i:
			print(j[0],j[1],end=" ")
		print()
