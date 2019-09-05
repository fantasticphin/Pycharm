a = list(map(float, input().split()))
b = [int(y) for y in a]
for x in a:
    if x == 0:
        a = sum(a[:-1])
    else:
        continue
print(sum(b))
print('{0:0.2f}'.format(a))
