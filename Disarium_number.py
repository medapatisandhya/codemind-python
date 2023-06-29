import math
n=int(input())
d=len(str(n))
t=n
s=0
for i in range(d,0,-1):
    r=n%10
    s=s+math.pow(r,i)
    n=n//10
if s==t:
    print(True)
else:
    print(False)