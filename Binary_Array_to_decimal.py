import math
n=int(input())
l=list(map(int,input().split()))
r,b=0,1
for i in range(n-1,-1,-1):
    r+=l[(n-1)-i]*math.pow(2,i)
print(int(r))