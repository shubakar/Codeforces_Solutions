for _ in range(int(input())):
    n,m=input().split()
    n=int(n)
    m=int(m)
    l=[]
    for i in range(n):
        l.append(list(map(int,input().split())))
    ans=0
    temp=[[0,0] for i in range(n+m-1)]
    for i in range(n):
        for j in range(m):
            temp[i+j][l[i][j]]+=1
    low=0
    high=n+m-2
    while low<high:
        #print(temp[low][0]+temp[high][0],temp[low][1]+temp[high][1])
        ans+=min(temp[low][0]+temp[high][0],temp[low][1]+temp[high][1])
        low+=1
        high-=1
    print(ans)
