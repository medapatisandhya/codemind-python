n=int(input())
ar=list(map(int,input().split()))
l=[]
for i in ar:
    l.append(i*i)
l.sort()
for i in l:
    print(i,end=" ")