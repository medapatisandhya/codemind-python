n=int(input())
l=list(map(int,input().split()))
k=int(input())
d={}
c=0
for i in l:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
for i in d:
    if d[i]==k:
        print(i,end=" ")
        c+=1
if(c==0):
    print("-1")