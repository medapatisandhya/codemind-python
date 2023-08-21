n=int(input())
arr=list(map(int,input().split()))
for i in range(0,n):
    c=0
    for j in range(0,n):
        if arr[j]<arr[i]and j!=i:
            c+=1
    print(c,end=" ")