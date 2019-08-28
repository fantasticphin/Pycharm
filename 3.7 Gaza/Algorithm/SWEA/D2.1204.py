# for t in range(int(input())):
#     n = input()
#     n = list(map(int, input().split()))
#     m = 0
#     k = 0
#     for x in set(n):
#         if n.count(x) > m:
#             m = n.count(x)
#             k = x
#     print(f'#{t+1} {k}')

a = [10, 8, 7, 2, 2, 4, 8, 8, 8, 9, 5, 5, 3]
print(set(a))