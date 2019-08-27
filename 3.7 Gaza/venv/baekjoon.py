# print(f'Hello World!')
# a = '강한친구 대한육군'

# a, b = map(int, input().split())
# print(a+b)

# def my_sqrt(n):
#     x, y = 1, n #양의 정수 => 1 ~ n
#     result = 1 #우리가 추측하는 제곱근의 근사값
#     #while not math.isclose(result ** 2, n):
#     while abs(result**2 - n) > 0.000000000001:
#         #제곱근 제곱과 입력 값의 차이가 저거도 0.0000000001보다 작아지면 그 차이가
#         #거의 없다고 봄
#         result = (x+y) / 2
#         # 양쪽 끝 값의 절반을 다시 제곱근의 근사치로 봄
#         if result ** 2 < n:
#             x = result
#         else:
#             y = result
#     return result
#
# print(my_sqrt(2))
# 1.4142135623733338
#
# import math
# print(math.sqrt(2))

# a = input()
# def decimal():
#     for i in a:
#         if i == int:
#             print('정수입니다.')
#     else:
#         print('소수입니다.')
#     return ()
# a=int(input())
# b=[1,1,]
# for i in range(2,a):
#     b.append(b[i-2]+b[i-1])
#
# print(b)

# #calc.py
# def addi(num1, num2):
#     result = num1 + num2
#     return result
#
# def subi(num1, num2):
#     result = num1 - num2
#     return result
#
# def multi(num1, num2):
#     result = num1 * num2
#     return result
#
# def divi(num1, num2):
#     try:
#         result = num1 / num2
#     except ZeroDivisionError:
#         return ('0 으로는 나눌 수 없습니다')
#     else:
#         return result
#
# print(addi(1, 3))
# print(subi(10, 4))
# print(multi(4, 2))
# print(divi(10, 0))

# result = 0
#
# def add(n):
#     global result
#     result += n
#     return result
# print(add(10))
# print(add(5))

# class Circle:
#     pi = 3.14
#     x = 2
#     y = 3
#     r = 3
#
#     def __init__(self, x, y, r):
#         self.r = 3
#         self.x = 2
#         self.y = 3
#
#     def area(self):
#         return self.pi * self.r * self.r
#
#     def circumference(self):
#         return 2 * self.pi * self.r
#
#     def center(self):
#         return (self.x, self.y)
#
#
# cir = Circle(3,2,4)
# print(cir.area())
# print(cir.circumference())
# j = 0
# for i in range(6):
#     while j < 5:
#         j += 1
#         print('*' * j)
#
# class Calculator:
#     count = 0
#
#     def info(self):
#         print('나는 계싼기 입니다')
#
#     @staticmethod
#     def add(a, b):
#         Calculator.count += 1
#         print('{} + {} 는 {} 입니다.'.format(a,b, a+b))
#
#     @classmethod
#     def history(cls):
#         print('총 {}번 계산 했습니다'.format(cls.count))
#
# C1 = Calculator()
# C1.info()
# C1.add(5,5)
# Calculator.history()

# strings = 'PYTHON'
# print(strings[::-1])

# phone_number = '010-1111-2222'
# ph2 = phone_number.replace('-', ' ')
# print(ph2)
# ph3 = ph2 (' ', '')

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# new_number = [n for n in numbers if n%2 == 1]
# new_number2 = [new_number[-1]]
# print(new_number2)

# n = int(input())
# # print(int(n)+int(n*2)+int(n*3)+int(n*4))
# a = n*1
# b = a+ n*10
#
# n*1 + n*11 + n*111 + n*1111

# def positive_sum(numbers):
#     new_list =[]
#     for i in numbers:
#         if i >= 0:
#             new_list.append(i)
#     result = sum(new_list)
#     # new_list = sum([i for i in numbers if i >= 0])
#     return result
# print(positive_sum([1,2,4,6,7,-2,-2,-1,-2,0,-3,4]))
# print(positive_sum([-4,-1,-2,-3,-2,-5]))

# def calc(equation):
#     eq_rep=equation.replace('+', ' +').replace('-', ' -')
#     eq_spl=eq_rep.split()
#     eq_list=list(map(int,eq_spl))
#     result = sum(eq_list)
#     return result
# print(calc('123+2-124'))
# print(calc('-12+12-7979+9191'))
# print(calc('+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1'))

# class Point:
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def __str__(self):
#         return ('Point : ({},{})'.format(self.x, self.y))
#
# # p1 = Point(3,5)
# # print(p1)
#
#
# class Circle:
#     pi = 3.14
#
#     def __init__(self, center, r):
#         self.r = r
#         self.center = center
#
#     def get_area(self):
#         return Circle.pi * self.r**2
#
#     def get_perimeter(self):
#         return 2 * Circle.pi * self.r
#
#     def get_center(self):
#         return self.center.x, self.center.y
#
#     def __str__(self):
#         return ('Circle:({},{},r:{})'.format(self.center.x, self.center.y, self.r))
#
# p1 = Point(0, 0)
# c1 = Circle(p1, 3)
# print(c1.get_area())
# print(c1.get_perimeter())
# print(c1.get_center())
# print(c1)
# p2 = Point(4, 5)
# c2 = Circle(p2, 1)
# print(c2.get_area())
# print(c2.get_perimeter())
# print(c2.get_center())
# print(c2)

# def calc(word):
#     new_list = {}
#     for x in word:
#         new_list[x]=0
#     for k in word:
#         new_list[x] += 1
#     return new_list
# print(calc('hello'))

# list1 = ['a', 'c', 'd', 'b', 'e']
# print(sorted(list1))
# list1.reverse()
# print(list1)

# list2 = [1,2,3,4,5,6,7,8,9]
# list2.split(' ')

# class phoneBook(object):
#     def __init__(self, name, number, religion, photo):
#         self.name = name
#         self.number = number
#         self.religion = religion
#         self.photo = photo
#         print(f'{self.name},{self.number},{self.religion},{self.photo} your info is saved.')
#
#
# def show_data(self):
#     print(self.name, self.number, self.religion, self.photo)
#
#
# def make_call(self):
#     return (f'{self.name}의 연락처는 {self.number}입니다.')
#
#
# class bestfriend(phoneBook):
#
#     def bff(self):
#         print(f'{self.name}의 연락처는 {self.number}입니다.')
#
#     def cal_call(self):
#         cal_cnt = 0
#         for c in self:
#             cal_cnt += 1
#         return (cal_cnt)
#
# p1 = phoneBook('gaga', 123421314, 'christian', 'notavail')
# p2 = phoneBook('gogo', 412341232, 'catholic', 'notavail')
# p3 = phoneBook('gugu', 568948287, 'buddhism', 'avail')
# p1.show_data()

# s = (1,2,3)
# s = list(s)
# s.append(4)
# s = tuple(s)
# print(s)

# s = (10,20,30)
# print(len(s), sum(s))

# num = (3,)
# num = 3,
# print(type(num))

# d = 'FIFA 2018'
# b = d[5:]
# b = int(b)
# print(b)

# 왼쪽으로 붙은 직각 삼각형 별 만들기
# for k in range(0,-6, -1):
#     print('*' * k)
# 별 역순 찍기
# a = 6
# while a >= 0:
#     a -= 1
#     print('*' * a)

# 별 찍기
# a = 0
# while a < 5:
#     a += 1
#     print(a * "*")

# 오른쪽 별 찍기
# a = 0
# while a < 5:
#     a += 1
#     b = 5-a
#     print(' '*b, '*' * a)

# a = [1,2,3,4,3,2,1]
# def s_l (a):
#     b = set(a)
#     c = sorted(list(b))
#     return c
# print(s_l(a))

# a = [2, 4, 6, 8, 10]
# b = 5
# c = 10
# def taehan(a,b):
#     if b in a:
#         return '{} => True'.format(b)
#     else:
#         return '{} => False'.format(b)
#
# print(a)
# print(taehan(a,b))
# print(taehan(a,c))

# a = 10
# b = 0
#
# def countdown(x):
#     if x <= 0:
#         print('카운트다운을 하려면 {}보다 큰 입력이 필요합니다.'.format(x))
#     else:
#         for i in range(x, 0, -1):
#             print(i)
#
# countdown(b)
# countdown(a)
#
# a = list(filter(lambda x: x % 2 ==0 ,range(1,11)))
# print(a)
# a,b,c,d,e = map(int, list(input()))
# f = sum([a,b,c,d,e])
# print(f)

# a = int(input())
# b = 0
# for i in range(1, a+1):
#     if a % i == 0:
#         b = i
#         print(b, end=' ')

# def calculate(a,b):
#     return a+b, a-b, a*b, int(a/b)
#
# print(calculate(8,3))
#
# T = int(input())
# x = map(int, input().split())
# def oddi(x):
#     ls =[i for i in range(x) if i % 2 !=0]
#     lf = sum(ls)
#     return lf
#
# print('# {} {}'.format(T, oddi(x)))

# a = max(477162, 658880, 751280, 927930, 297191)
# b = min(477162, 658880, 751280, 927930, 297191)
# print(a - b)

# a = list(map(int,input().split( )))
# print(a)

# for i in range(5):
#     for j in range(5):
#         print(''*j)
#         for k in range(5):
#             print('*'*(k - j))
#
# for i in range(5):
#     print(' '*i, end='')
#     print('*'*(5-i), end='')
#     print()
# for i in range(5):
#     for x in range(i):
#         print(' ', end='')
#     for x in range(5-i):
#         print('*', end='')
#     print()

# def charst(a):
#     for i in a:
#         print(ord(i)-64, end=' ')
#
# a = input()
# charst(a)
#
# a = list(map(int,input()))
# b = 0
# for x in a:
#     b += x
# print(b)

# T = int(input())
#
# for tc in range(1, T + 1):
#     li = list(map(int, input().split()))
#     li_max = li[0]
#
#     for i in li:
#         if i > li_max:
#             li_max = i
#
#     print('#{} {}'.format(tc, li_max))

# bit = [0,0,0,0]
# for i in range(2):
#     bit[0] = i
#     for j in range(2):
#         bit[1] = j
#         for k in range(2):
#             bit[2] = k
#             for l in range(2):
#                 bit[3] = l
#                 print(bit)

# arr = [3,6,7,1,5,4]
#
# n = len(arr) #n은 원소의 개수
#
# for i in range(1<<n): # 1<<n: 부분 집합의 개수
#     for j in range(n+1): #원소의 개수만큼 비트를 비교
#         if i & (1<<j): # i의 j번째 비트가 1이면 j번째 원소 출력
#             print(arr[j], end=', ')
#     print()
# print()

# i = int(input())
# for x in range(1, i+1):
#     print(x, end=' ')

# 정수를 입력받다가 0 이 입력되면 그 때까지 입력받은 홀수의 개수와 짝수의 개수를 출력하는 프로그램을 작성하시오.

# i = list(map(int, input().split()))
# odd = 0
# even = 0
#
# for x in i:
#
#     if x % 2 == 0 and x != 0:
#         even += 1
#
#     elif x % 2 != 0:
#         odd += 1
#
#
#
# print('odd : {}'.format(odd))
# print('even : {}'.format(even))

# for x in range(10, 21):
#     print(x, end=' ')

# 하나의 정수를 입력받아 1부터 입력받은 정수까지의 짝수를 차례대로 출력하는 프로그램을 작성하시오. 입력되는 정수는 50이하이다.

# a = int(input())
# for x in range(1, a+1):
#     if x % 2 == 0:
#         print(x, end=' ')

# a = int(input())
# for x in range(a):
#     print('#' * x, end='')

# for x in range(5):
#     for j in range(5):
#         if x == j:
#             print('#', end='')
#         else:
#             print('+', end='')
#     print()

# a = list(map(int, input().split()))
# t = 0
# f = 0
# for x in a:
#     if x % 3 == 0:
#         t += 1
#     if x % 5 == 0:
#         f += 1
# print('Multiples of 3 : {}'.format(t))
# print('Multiples of 5 : {}'.format(f))

# a = int(input())
# b = list(map(int, input().split()))
# c = 0
# avgs = 0
# for x in b:
#     c += x
#     avgs = round(c/len(b),2)
# print('avg : {}'.format(avgs))
# if avgs >= 80:
#     print('pass')
# else:
#     print('fail')

# for i in range(2, 7):
#     for j in range(i+1, i+5):

# T = int(input())
# for tc in range(1, T+1):
#     namba = list(map(int, input().split()))
#     bf_sums = []
#     sums = 0
#     for i in namba:
#         if i % 2 != 0:
#             bf_sums.append(i)
#         sums = sum(bf_sums)
#
#     print('#{} {}'.format(tc, sums))

# T = int(input())
# data = list(map(int, input().split()))
# data_sor = sorted(data)
# print(data_sor[T//2])

# def BubbleSort(L):
#     k = 0
#     for i in range(len(L)-1):
#         if L[i] > L[i+1]:
#             L[i], L[i+1] = L[i+1], L[i]
#             k += 1
#     return k
#
# T = int(input())
# data = list(map(int, input().split()))
# print(BubbleSort(data))
# print(BubbleSort(data)[T//2])

# N = list(map(int, input().split(',')))
# print(list(N))
# print(tuple(N))
#
# N = list(map(int, input().split(',')))
# NS = []
# pi = 3.1415
# for i in N:
#     NS.append(round((2 * pi * i),2))
# for i in NS:
#     print(int(i))

# n = int(input())
# for i in range(n+2, 0, -2):
#     print(' '*((n+2-i)//2) + '*' * i)
#
#별그리기 별별볇렵려
# for i in range(0, 3, 1):
#     for j in range(i, 2, 1):
#         print(" ", end="")
#     for j in range(0, i + 1, 1):
#         print("*", end="")
#     print()
#
# for i in range(0, 3, 1):
#     for j in range(0, i, 1):
#         print(" ", end="")
#     for j in range(3, i, -1):
#         print("*", end="")
#     print()
# N = 20
# cnt = 0
# for i in range(1, N+1):
#     if i % 3 == 0:
#         cnt += 1
# print(cnt)

# def recur_A(n):
#     if n == 1:
#         return 0
#     return recur_A(n-1) + 2
#
# print(recur_A(10))

# arr = [1, 1, 3, 3, 0, 1, 1]
#
# def sortss(n):
#     answ = []
#     for i in range(n):
#
# print(sortss(arr))

N = list(map(int, input().split(',')))
NS = []
pi = 3.1415
for i in N:
    NS.append(str(round((2 * pi * i),2)))

a = ', '.join(NS)
print(a)