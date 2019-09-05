a,b = map(int,input().split())
for i in range(a, b+1, 2):
    print(i, end=' ')
print()
for j in range(b, a-1, -2):
    print(j, end=' ')
print()