def rsum(n):
    if n == 1:
        return 1
    else:
        return n + rsum(n-1)

print(rsum(10))