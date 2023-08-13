def even(n):
    c=0
    while n!=0:
        r=n%10
        c+=1
        n=n//10
    return c
n=int(input())
l=list(map(int,input().split()))
s=0
for i in l:
    if even(i)%2==0:
        s+=1
print(s)