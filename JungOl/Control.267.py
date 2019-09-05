x = list(map(int,input().split()))
b = [a for a in x if a % 3 == 0]
if b == []:
    print(0)
for z in b:
    print(z, end=' ')

