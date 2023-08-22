def palin(n):
    t,s=n,0
    while n!=0:
        r=n%10
        s=s*10+r
        n=n//10
    if s==t:
        return 1
s=int(input())
e=int(input())
for i in range(s,e+1):
    if palin(i)==1:
        print(i,end=" ")