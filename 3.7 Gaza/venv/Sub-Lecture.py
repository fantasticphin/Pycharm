#
# dict_repr = {
# 'Mary': {'Korean': 80, 'Math': 65, 'English': 58},
# 'Peter': {'Korean': 60, 'Math': 95, 'English': 72},
# 'John': {'Korean': 70, 'Math': 78, 'English': 69}
# }
# def solution(dic, ky, ct):
#     scholar = []
#     for nam,sco in dic.items():
#         if sco.get(ky) >= ct:
#             scholar.append(nam)
#     return sorted(scholar)
# print(solution(dict_repr, 'Math', 70))
#
# def solution2(dic, ky, ct):
#     return sorted([nam for nam,sco in dic.items() if sco.get(ky) >= ct])
# print(solution2(dict_repr, 'Korean',70))

# a = 1
# while a < 16:
#     print(a, end=' ')
#     a += 1

# def calccent(a):
#     return a*(a + 1)//2
#
# print(calccent(10))

# a = int(input())
# b = 0
# while b < a:
#     b = a*(a+1)//2
# print(b)

# while True:
#     a = int(input('number? '))
#     if a < 0:
#         print('negative number')
#     if a > 0:
#         print('positive integer')
#     if a == 0:
#         break

# nums = input()
# i = 0
# nums_str = nums.split()
# num_list = list(nums_str)
# sums = 0
#
# while True:
#     sums += list[i]
#     i += 1
#     if list[i-1] >= 100:
#         break
# print(sums)
# while True:
#     a = int(input())
#     if a == -1:
#         break
#     if a % 3 == 0:
#         print(a // 3)
#     if a % 3 != 0:
#         continue