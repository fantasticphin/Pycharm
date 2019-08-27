# 01.workshop

# n = 5
# m = 9

# print((( n * "*") + '\n') * m)

# a = '*' + " " * (n-2) + '*'
#
# print('*' * n, end='')
# print(('\n' + a) * m)
# print('*'*n)

# print('"파일은 C:\\Windows\\Users\\내문서\\Python에 저장이 되어있습니다." \n나는 생각했다. \'cd를 써서 git bash로 들어가봐야지\'')

# a = 1
# b = 4
# c = -21
#
# print((-b + (b**2 -4*a*c)**(1/2)) / 2*a)
# print((-b - (b**2 -4*a*c)**(1/2)) / 2*a)

#  01_Homework
# a = 0.1 * 3
#  b = 0.3
# #print(round(a,3) == b)

# name = "철수"
# print("'안녕, %s야'" % name)
# print("\"안녕, {}야.\"" .format(name))

# print(float('3.5'))
# print(float('30'))

# a = 5
# i = 0
# while i < 5:
#     print('*' * (a-i))
#     i += 1

# a = int(input())
# b = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# c = b.count(a)
# if a < 9:
#     print("{0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}".format(c))

# import keyword
# print(keyword.kwlist)

# 02_workshop
#1 직사각형 별 찍기
# n = 5
# m = 9
# for i in range(m):
#     for j in range(n):
#         print('*', end='')
#     print('')
#2 딕셔너리 평균
# student = {'python' : 80, 'algorithm': 99, 'django': 89, 'flask': 83}
# avg = (student['python'] + student['algorithm'] + student['django'] + student['flask']) /len(student)
# print(avg)
# avg = sum(students.values()) / len(student)
#3 혈액형 집계
# blood_types = ['A', 'B', 'A', 'O', 'AB', 'AB', 'O', 'A', 'B', 'O', 'B', 'AB']
# blood_dict = {'A': 0, 'B': 0, 'AB': 0, 'O': 0}
# for bt in blood_types:
#     for key in blood_dict.keys():
#         if bt == key:
#             blood_dict[key]+=1
# print(blood_dict)

# l = list(range(1,51))
# print(l[::2])