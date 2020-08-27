import math
for _ in range(int(input())):
	n=int(input())
	ans=""
	temp=math.ceil(n/4)
	for i in range(n-temp):
		ans+="9"
	for i in range(temp):
		ans+="8"
	print(ans)
