n,m=map(int,input().split())
for i in range(1,max(n,m)):
    if n%i==0 and m%i==0:
        s=i
print(s)