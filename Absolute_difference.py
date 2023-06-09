def primes(n):
    if n==1:
        return 0
    for i in range(2,(n//2)):
        if n%i==0:
            return 0
    return 1
n=int(input())
arr=list(map(int,input().split()))
s,c=1,1
for i in arr:
    if primes(i)==1:
        s*=i
    else:
        c*=i
m=abs(s-c)
print(m)