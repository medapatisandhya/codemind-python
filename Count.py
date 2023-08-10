n=int(input())
li=list(map(int,input().split()))
c,a=0,0
for i in li:
    if i%2==0:
        c+=1
    else:
        a+=1
print(c,a)