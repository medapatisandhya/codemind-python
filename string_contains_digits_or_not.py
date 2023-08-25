n=int(input())
for i in range(0,n):
    s=input()
    c=0
    for i in s:
        if i>='0' and i<'9':
            c+=1
            break
    if c==0:
        print("No")
    else:
        print("Yes")