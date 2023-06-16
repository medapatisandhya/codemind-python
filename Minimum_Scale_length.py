n=int(input())
ar=list(map(int,input().split()))
gcd=ar[0]
j=1
while j<n:
    if ar[j]%gcd==0:
        j+=1
    else:
        gcd=ar[j]%gcd
print(gcd)