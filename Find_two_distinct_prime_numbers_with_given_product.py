n=int(input())
s=1
for i in range(2,n):
    if n%i==0:
        s=s*i
        print(i,end=" ")
if s!=n:
    print("-1")
        