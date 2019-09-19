def fact(n):
    rst = 1
    for i in range(1, n+1):
        rst *= i
    return rst

def fact2(n):
    if n <= 1:
        return 1
    else:
        return n * fact2(n-1)

print(fact(4))
print(fact2(4))