for _ in range(int(input())):
	n=int(input())
	l=list(map(int,input().split()))
	peak=n-1
	while peak>0 and l[peak-1]>=l[peak]:
		peak-=1
	while peak>0 and l[peak-1]<=l[peak]:
		peak-=1
	print(peak)
	
