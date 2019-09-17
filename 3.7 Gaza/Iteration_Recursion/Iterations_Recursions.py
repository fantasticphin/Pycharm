# i = 0
# while i < 10:
#     print(i)
#     i += 1

# for i in range(10):
#     print(i)
#     i += 3
#
# i = 100
# while True:
#     print(i)
#     i += 1
#     if i >= 10:break
# print(i)

# A = [10, 0, 2, 410, 22, 50]
# def selsort(A):
#     for i in range(0, len(A)):
#         min = i
#         for j in range(i+1, len(A), 1):
#             if A[j] < A[min]:
#                 min = j
#         A[i], A[min] = A[min], A[i]
#     return A
# print(selsort(A))

# def facts(n):
#     rst = 1
#     for i in range(1, n +1):
#         rst *= i
#     return rst
# print(facts(5))
#
# def fact(n):
#     if n <= 1:
#         return 1
#     else:
#         return n * fact(n-1)
# print(fact(5))

# def power(k):
#     i = 0:
#     power = 1
#     while i < k:
#         power *= 2
#         i += 1
#     return power

# def tenten(x):
#     if x == 1:
#         return 1
#     else:
#         return x + tenten(x-1)
#
# print(tenten(10))

# ary = [5,2,7,1,3,8,9,3,5,2]
# def recselsort(ary, st, ed):
#     if st == ed:
#         return
#     else:
#         mins = st
#         for j in range(st, ed, 1):
#             if ary[j] < ary[mins]:
#                 mins = j
#
#         ary[st], ary[mins] = ary[mins], ary[st]
#         recselsort(ary, st+1, ed)
# recselsort(ary, 0, len(ary))
# print(ary)
# a = 124783
# b = 667767
# c = 054060
# d = 101123

# def babygin():
#     global flag
#     check = 0
#     if arr[0] == arr[1] and arr[1] == arr[2]: check += 1
#     if arr[3] == arr[4] and arr[4] == arr[5]: check += 1
#
#     if arr[0] + 1 == arr[1] and arr[1] + 1 == arr[2]: check += 1
#     if arr[3] + 1 == arr[4] and arr[4] + 1 == arr[5]: check += 1
#
#     if check == 2:
#         flag = 1
#         return
#
#
# def perms(n,k):
#     if flag == 1: return
#
#     if k == n:
#     babygin()
#     else:
#         for i in range(k, n):
#             arr[k], arr[i] = arr[i],arr[k]
#             perm(n,k+1)
#             arr[k], arr[i] = arr[i],arr[k]
#
# flag = 0
# perm(6,0)

# def myprint(q):
#     while q != 0:
#         q = q-1
#         print('{}'.format(t[q]), end=' ')
#     print()
#
# def perm(n,r,q):
#     if r ==0:
#         myprint(q)
#     else:
#         for i in range(n-1, -1, -1):
#             a[i], a[n-1] = a[n-1], a[i]
#             t[r-1] = a[n-1]
#             perm(n-1, r-1, q)
#             a[i], a[n-1] = a[n-1], a[i]
#
# a = [1,2,3]
# t = [0] * 3
#
# perm(3,2,2)

# def myP(q):
#     for i in range(q):
#         print('{}'.format(T[i]),end=' ')
#     print()
#
# def combs(n,r,q):
#     if r == 0:
#         myP(q)
#     elif n < r:
#         return
#     else:
#         T[r-1] = A[n-1]
#         combs(n-1, r-1, q)
#         combs(n-1, r, q)
#
# A = [1,2,3,4]
# T = [0] * 3
#
# combs(4,3,3)

#중복조합
# def myP(q):
#     for i in range(q):
#         print('{}'.format(T[i]),end=' ')
#     print()
#
# def combs(n,r,q):
#     if r == 0:
#         myP(q)
#     elif n == 0:
#         return
#     else:
#         T[r-1] = A[n-1]
#         combs(n, r-1, q)
#         combs(n-1, r, q)
#
# A = [1,2,3,4]
# T = [0] * 3
#
# combs(4,3,3)
# A = {1,2,3,4,5,6,7,8,9,10}
# N = len(A)
#
# def subset(p,q):
#     for i in range(0, N):
#         for j in range(0, N):
#             if i & (1<<j):
#             print('{}'.format(p[j]), end=' ')

data = [1,2,3,4,5,6,7,8,9,10]
A = [0] * len(data)

# def printS(n):
#     for i in range(n):
#         if A[i] == 1:
#             print('{}'.format(data[i]), end=' ')
#     print()
#
# def powS(n,k):
#     if n == k:
#
#         printS(n)
#     else:
#         A[k] = 1
#         powS(n,k+1)
#         A[k] = 0
#         powS(n,k+1)
#
# powS(data,10)

def printS(n):
    global count
    sum = 0
    for i in range(n):
        if A[i] == 1:
            print('{}'.format(data[i]), end=' ')
    print()


def powS(n, k):
    if n == k:

        printS(n)
    else:
        A[k] = 1
        powS(n, k + 1)
        A[k] = 0
        powS(n, k + 1)


powS(data, 10)