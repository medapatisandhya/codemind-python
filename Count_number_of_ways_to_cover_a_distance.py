def count_ways(n):
    if n<0:
        return 0
    if n==0:
        return 1
    return count_ways(n-1)+count_ways(n-2)+count_ways(n-3)
n=int(input())
c=count_ways(n)
print(c)