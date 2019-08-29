# for t in range(int(input())):
#     n = int(input())
#     m = [[0 for i in range(n)]for j in range(n)]
#     a = 1
#     L = 0
#     for k in range(n, 0, -1):
#         for i in range(L, k):
#             m[L][i] = a
#             a += 1
#         for i in range(L+1, k):
#             m[i][k-1] = a
#             a += 1
#         for i in range(k-2, L-1, -1):
#             m[k-1][i] = a
#             a += 1
#         for i in range(k-2, L, -1):
#             m[i][L] = a
#             a += 1
#         L += 1
#     print('#{}'.format(t+1))
#     for j in range(n):
#         c = list(map(str,m[j]))
#         print(' '.join(c))

n = int(input())

for y in range(0, n):
    for x in range(0, n):
        p = min(x, y, n - x - 1, n - y - 1)
        if x >= y:
            q = x + y - 2 * p
        else:
            q = (n - 1 - 2 * p) * 4 - (x + y - 2 * p)
        q += 4 * (p * n - (p * p))
        print("{:3d}".format(q+1), end="")
    print()