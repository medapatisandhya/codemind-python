n=int(input())
l=list(map(int,input().split()))
sumi=0
for i in l:
    sumi+=i
sumi=sumi/n
print(format(sumi,".2f"))
