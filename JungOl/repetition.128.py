a = list(map(int,input().split()))
for x in a:
    if x == 0:
        a.pop(-1)
b = [x for x in a if x % 3 != 0 and x % 5 != 0]
print(len(b))