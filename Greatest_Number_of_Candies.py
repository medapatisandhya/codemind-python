n=int(input())
arr=list(map(int,input().split()))
l=int(input())
maxi=max(arr)
for i in arr:
    if(i+l)>=maxi:
        print(True,end=" ")
    else:
        print(False,end=" ")