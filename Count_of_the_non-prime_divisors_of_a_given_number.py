import math
def prime(x):
    if(x==1):
        return -1
    else:
        for i in range(2,int(math.sqrt(x))+1):
            if(x%i==0):
                return -1
    return 1
n=int(input())
c=0
for i in range(1,n+1):
    if(n%i==0 and prime(i)==-1):
        c+=1
print(c)