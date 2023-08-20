def sub(s):
    c,m=0,0
    for i in s:
        if i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
            c+=1
        else:
            if m<c:
                m=c
                c=0
            else:
                continue
    return m
s=input()
r=sub(s)
print(r)