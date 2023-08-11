l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
s,m=0,0
for i in range(0,3):
    if l1[i]>l2[i]:
        s+=1
    if l1[i]<l2[i]:
        m+=1
print(s,m,end=" ")
