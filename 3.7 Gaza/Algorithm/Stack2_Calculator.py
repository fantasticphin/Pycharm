# def pop(s):
#     if len(s) == 0:
#         return
#     else:
#         return s.pop(-1)
#
#
# str = '2+3*4/5'
# stack = []
#
# for i in range(len(str)):
#     if str[i] == '+' or str[i] == '-' or str[i] =='*' or str[i] == '/':
#         stack.append(str[i])
#     else:
#         print(str[i], end="")
#
# while len(stack) != 0:
#     print(stack.pop(), end="")


#powerset 부분집합
# cnt = 0
# N = 3
# A = [0 for _ in range(N)]
#
# def printset(a):
#     global cnt
#     cnt += 1
#     print('%d : '%(cnt), end="")
#     for i in range(n):
#         if A[i] == 1:
#             print('%d '%(data[i]), end="")
#     print()
#
# def powerset(n,k):
#     if n == k:
#         printset(n)
#     else:
#         A[k] =1
#         powerset(n, k +1)
#         A[k] =0
#         powerset(n, k +1)
#
# powerset(N,0)

# count = 0
# total = 0
# N = 10
# A = [0 for _ in range(N)]
# data = [1,2,3,4,5,6,7,8,9,10]
#
# def printset(n):
#     global count
#     sum = 0
#     for i in range(n):
#         if A[i] == 1:
#             sum += data[i]
#
#     if sum == 10:
#         count += 1
#         print('{} : '.format(count), end="")
#         for i in range(n):
#             if A[i] == 1:
#                 print('{} '.format(data[i]),end="")
#         print()

# def powerset(n,k):
#     global total
#     total += 1
#     if n == k:
#          printset(n)
#     else:
#         A[k] =1
#         powerset(n, k +1)
#         A[k] =0
#         powerset(n, k +1)
#
#
# print(powerset(N,0))
# print('호출횟수 : {}'.format(total))


# def powerset(n,k,sums):
#     global total
#     if sums > 10: return
#     total += 1
#     if n == k:
#         printset(n,sums)
#     else:
#         A[k] = 1
#         powerset(n,k+1, sums + data[k])
#         A[k] = 0
#         powerset(n, k + 1, sums)
#
# powerset(N, 0, 0)
# print('호출횟수 : {}'.format(total), end='')

#재귀함수 순열 생성

# def babyGin(n):
#     global flag
#     check = 0
#
#     if arr[0] == arr[1] and arr[1] == arr[2]: check +=1
#     if arr[3] == arr[4] and arr[4] == arr[5]: check +=1
#
#     if arr[0] + 1 == arr[1] and arr[1] + 1 == arr[2]: check +=1
#     if arr[3] + 1 == arr[4] and arr[4] + 1 == arr[5]: check +=1
#
#     if check == 2:
#         flag = 1
#         return
#
# def perm(n,k):
#     if k == n:
#         babyGin(n)
#     else:
#         for i in range(k,n):
#             arr[k], arr[i] = arr[i], arr[k] #스왑 작업
#             perm(n, k + 1)
#             arr[k], arr[i] = arr[i], arr[k] #스왑 작업

# arr = [1,2,4,7,8,3]
# arr = [6,6,7,7,6,7]
# arr = [0,5,4,0,6,0]
# arr = [1,0,1,1,2,3]
# flag = 0
# perm(6,0)
#
# if flag:
#     print('BabyGin')
# else:
#     print('Not BabyGin')

def jegop(b,e):
    result = 1
    for i in range(e):
        result *= b
    return result
print(jegop(2,10))

#분할 정복
def power(be, exp):
    if exp == 0 or be == 0:
        return 1
    if exp % 2 == 0:
        NeBe = power(be, exp/2)
        return NeBe * NeBe
    else:
        NeBe = power(be, (exp-1)/2)
        return (NeBe * NeBe) * be

print(power(2,4))