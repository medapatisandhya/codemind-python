n=int(input())
i=[]
while n!=0:
    r=n%10
    i.append(r)
    n=n//10
print(max(i))