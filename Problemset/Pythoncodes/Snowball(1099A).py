def cal(s,e):
	return ((s*(s+1))//2)-((e*(e+1))//2)
w,h=map(int,input().split())
u1,d1=map(int,input().split())
u2,d2=map(int,input().split())
if d2>d1:
	d1,d2=d2,d1
	u1,u2=u2,u1
w+=cal(h,d1-1)
w=max(0,w-u1)
w+=cal(d1-1,d2-1)
w=max(0,w-u2)
w+=cal(d2-1,0)
print(w)
