n,m=map(int,input().split())
mu="x"
e="="
for i in range(1,m+1):
    if i%2!=0:
        print(n,mu,i,e,n*i)