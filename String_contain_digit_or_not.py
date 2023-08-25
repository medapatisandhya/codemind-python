s=input()
c=0
for i in s:
    if i>='0' and i<='9':
        c+=1
if c==0:
    print("Doesn't contain digit")
else:
    print(f"Contains {c} digit")