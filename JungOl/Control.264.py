n = int(input())
for j in range(1):
    for i in range(1, 4):
        print('{} * {} = {:2}  '.format(n, i, n*i), end=" ")
    print()
    for i in range(4, 7):
        print('{} * {} = {:2}  '.format(n,i, n*i), end=" ")
    print()
    for i in range(7, 10):
        print('{} * {} = {:2}  '.format(n,i, n*i), end=" ")
    print()