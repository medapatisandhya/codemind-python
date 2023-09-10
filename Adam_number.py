n=int(input())
rev=str(n)[::-1]
nsq=n*n
revsq=int(rev)*int(rev)
if nsq==int(str(revsq)[::-1]):
    print(True)
else:
    print(False)