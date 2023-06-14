import math
p,r,t=map(int,input().split())
comp=p*(math.pow((1+(r/100)),t))
print("%.2f"%comp)