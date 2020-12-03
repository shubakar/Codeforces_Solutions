import math
def fu(A):
	if A==1:
		return 0
	if A==2:
		return 1
	if A==3:
		return 2
	if A%2==0:
		return 2
	return 3
for _ in range(int(input())):
	n=int(input())
	print(fu(n)
