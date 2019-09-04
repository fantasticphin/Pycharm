a = list(map(int,input().split()))
minmin = 9523123
for x in a:
    if x < minmin: minmin = x
print(minmin)