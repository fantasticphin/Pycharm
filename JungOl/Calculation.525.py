a = list(map(int,input().split()))

def highest(a):
    if a[0] > a[1] and a[0] > a[2]:
        return 1
    else:
        return 0

def equals(a):
    if a[0] == a[1] == a[2]:
        return 1
    else:
        return 0

print(highest(a), equals(a))
