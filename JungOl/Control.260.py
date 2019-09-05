a = list(map(int,input().split()))
b = 0
for i in a:
    if i == -1:
        print(b)
    elif i % 2 == 0:
        b += i
    else:
        b -= i