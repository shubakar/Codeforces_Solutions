n=int(input())
l=list(map(int,input().split()))
mi=l[0]
ma=l[0]
mi2=-1
ma2=-1
for i in range(1,n):
	if mi>l[i]:
		mi2=mi
		mi=l[i]
	elif mi2==-1 or mi2>l[i]:
		mi2=l[i]
	if l[i]>ma:
		ma2=ma
		ma=l[i]
	elif ma2==-1 or ma2<l[i]:
		ma2=l[i]
print(min(ma-mi2,ma2-mi))
