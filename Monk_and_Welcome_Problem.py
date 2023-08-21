n=int(input())
l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
l3,c=[],0
for i in range(0,n):
    c=l1[i]+l2[i]
    l3.append(c)
    c=0
for i in l3:
    print(i,end=" ")