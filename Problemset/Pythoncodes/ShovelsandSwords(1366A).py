for _ in range(int(input())):
    n,m=input().split()
    n=int(n)
    m=int(m)
    print(min(n,m,(n+m)//3))
