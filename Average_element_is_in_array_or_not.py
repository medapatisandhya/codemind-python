n=int(input())
lis=list(map(int,input().split()))
sumi=c=0
for i in lis:
    sumi+=i
sumi=sumi//n
for i in lis:
    if sumi==i:
        c=1
if(c==1):
    print(True)
else:
    print(False)