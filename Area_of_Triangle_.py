import math
A,B,C=map(int,input().split())
S=(A+B+C)/2
G=S*((S-A)*(S-B)*(S-C))
area=math.sqrt(G)
print("%.2f"%area)