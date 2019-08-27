#for i in range(1,100):
#   print(i)

# for i in range(1, 5):
#     print("*"*i)

# score = [88, 30, 61, 55, 95]
# students = range(5)
# for i in students:
#     if score[i] >= 60:
#         print('{}번 학생은 {}점으로 합격입니다.'.format(i+1,score[i]))
#     else:
#         print('{}번 학생은 {}점으로 불합격입니다.'.format(i+1, score[i]))

# score = [88, 30, 61, 55, 95]
# for i, k in enumerate(score):
#     if score[i] >= 60:
#         print('{}번 학생은 {}점으로 합격입니다.'.format(i+1,score[i]))
#     else:
#         print('{}번 학생은 {}점으로 불합격입니다.'.format(i+1, score[i]))

#가로나열
# list = range(1,101)
# for i in list:
#     if i%2==0:
#         print(i,end =' ')

#가로나열 홀수
# a = range(1,100, 2)
# b = ""
# for i in a:
#     b+=("{}, ".format(i))
# print(b[:-2])

# print(', '.join(map(str,list(range(1,100,2)))))

#1부터100 사이 3의배수 총합
# total = 0
# for i in range(100):
#     if i%3==0:
#         total += i
# print('1부터 100사이의 숫자 중 3의 배수의 총합: {}'.format(total))

#학생들 혈액형 데이터
# students = ['A', 'A', 'A', 'O', 'B', 'B', 'O', 'AB', 'AB', 'O']
# blood = students.count('A')
# blood1 = students.count('B')
# blood2 = students.count('AB')
# blood3 = students.count('O')
# print("{'A': %s, 'O': %s, 'B': %s, 'AB': %s}"%(blood,blood3,blood1,blood2))

#while 사용 시험성적 합산
# scores = [85, 65, 77, 83, 75, 22, 98, 88, 38, 100]
# s = 0
# while scores:
#         a = scores.pop()
#         if a >= 80:
#             s += a
# print(s)

#while 문 기초
# a = 0
# while a <= 100:
#     print(a)
#     a += 1

#if문 기초
# a = 6/3
# b = 3**3
# if a>b:
#     print(a)
# elif a==b:
#     print(a==b)
# else:
#     print(b)

#for문 기초
# saffy = ['Bae', 'Kim', 'Park', 'Ryu', 'Seo', 'Byeon']
# for x in saffy:
#     print('%s %s' % (x, len(x)))

#for문 range
a = [1,2,3,4,5,6,7,8,9]
for i in range(a):
    print(i)





