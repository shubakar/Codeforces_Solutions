for _ in range(int(input())):
    n,x,m=input().split()
    n=int(n)
    x=int(x)
    m=int(m)
    mi=x
    ma=x
    for i in range(m):
        l,r=input().split()
        l=int(l)
        r=int(r)
        if r<mi or l>ma:
            continue
        else:
            mi=min(mi,l)
            ma=max(ma,r)
    print(ma-mi+1)
