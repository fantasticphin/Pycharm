n = int(input())
for i in range(n):
    for j in range(i):
        print(' ', end='')
    for j in range(5-i*2, 0, -1):
        print('*', end='')
    print()