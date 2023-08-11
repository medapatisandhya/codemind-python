n=int(input())
for i in range(0,n):
    l=int(input())
    lis=list(map(int,input().split()))
    s=0
    for i in lis:
        s+=i
    m=(l*(l+1))//2
    print(m-s)