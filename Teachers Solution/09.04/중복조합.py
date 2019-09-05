# def myprin(q):
#     for i in range(q):
#         print('{}'.format(T[i]. end=" "))
#     print()
# def comb(n,r,q):
#     if r == 0:
#         myprin(q)
#     elif n < r:
#         return 0
#     else:
#         # T[r-1] = A[n-1]
#         return comb(n1, r-1, q) + comb(n-1, r, q)
# print(comb(4,3,3))

def comb(n,r):
    if r == 0:
        return 1
        # myprin(q)
    elif n < r:
        return 0
    else:
        # T[r-1] = A[n-1]
        return comb(n-1, r-1) + comb(n-1, r)

print(comb(1,4))