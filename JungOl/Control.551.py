n = int(input())
for t in range(n):
    for u in range(t):
        print(' ', end='')
    for u in range(n - t, 0, -1):
        print('*', end="")
    print()