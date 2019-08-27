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

# interest_0 = ['삼성전자', 'LG전자', 'SK Hynix']
# interest_1 = interest_0[:2]
# interest_1[0] = 'Naver'
# print(interest_0)

# t = 1,2,3,4
# print(type(t))

# interest = ['삼성전자', 'LG전자', 'SK Hynix']
# int2 = tuple(interest)
# print(type(int2))

# 튜플 데이터 개수와 동일한 상태에서 각 변수에 저장이 가능하다
# my_tuple = (1, 2, 3, 4)
# a, b, c = my_tuple
# print(a + b + c)

# *(star expression) 을 사용해 지정 개수 외에 값을 나타내지 않을 수 있음
# scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
# a,b,c,d,e,f,g,h,*i = scores
# print(a,b,c,d,e,f,g,h,*i)

# scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
# print(scores[1:9])
#
# temp = {'메로나': 1000, '폴라포': 1200, '빵빠레':1800 }
# temp['죠스바'] = 1200
# temp['월드콘'] = 1500
# print(temp)
# print(temp['메로나'])
# print(temp.get('메로나'))
# del temp['메로나']
# print(temp)

# # dictionary 생성
# inventory = {'메로나' : [300,20], '비비빅' : [400,3], '죠스바' : [250,100]}
# #메로나 밸류 1번째 불러오기
# price = inventory['메로나'][1]
# print('{} 개'.format(price))
# #딕셔너리에 새로운 키&값 넣기
# inventory['월드콘'] = [500, 7]
# print(inventory)
#
# k = inventory.keys()
# print(k)
# v = inventory.values()
# print(v)
# v1 = [v for v in inventory.values()]
# print(v1)
# v2 = v1[0][0], v1[1][0], v1[2][0], v1[3][0]
# print(sum(v2))

#가변형 인자로 정수들을 입력받아 곱을 반환하는 함수를 정의하고, 단, 1, 2, '4', 3와 같이 제대로 입력되지 않은 경우 예외를 처리하는 프로그램을 작성하십시오.#
# def trial(*a):
#     c = 1
#     for x in a:
#         if type(x) != int:
#             c='에러발생'
#             break
#         else:
#             c *= x
#     return c
# print(trial(5, 2, 3, 5, 1, 2, 3, 4))

# a = 65
# print('ASCII {} => {}'.format(a, chr(a)))

#1~10까지의 정수를 항목으로 갖는 리스트 객체에서 filter 함수와 람다식을 이용해, 짝수만을 선택해 리스트를 반환하는 프로그램을 작성하십시오.
# a = [i for i in range(1,11) if i % 2 == 0]
# print(a)
# a = list(map(lambda x: x**2, range(1,11)))
# print(a)

# 1~10까지의 정수를 항목으로 갖는 리스트 객체에서 filter 함수와 람다식을 이용해 짝수만을 선택한 후, map 함수와 람다식을 이용해 항목의 제곱 값을 갖는 리스트를 반환하는 프로그램을 작성하십시오.
# a = list(filter(lambda i: i % 2 == 0, range(1,11)))
#
# b = list(map(lambda x: x**2,a))
# print(b)

#가변형 인자를 전달 받아 가장 큰 값을 반환하는 함수를 정의하고,다음과 같은 결과를 출력하는 프로그램을 작성하십시오.
# max(3, 5, 4, 1, 8, 10, 2) => 10
# def maxi(*a):
#     cnt = 0
#     for i in a:
#         if i > cnt:
#             cnt = i
#     return cnt
#
# print(max(3, 5, 4, 1, 8, 10, 2))

# a = 'abcdef'
# b = 0,1,2,3,4,5
# c = (zip(a,b))
# print(type(b))

# a = 'abcdef'
# b = 0,1,2,3,4,5
# c = dict(zip(a,b))
# for k,v in c.items():
# 	print('{}:{}'.format(k,v))

# a = [ (90,80), (85, 75), (90, 100)]
# print('1번 학생의 총점은 '{}'점이고, 평균은 '{}'입니다.'.format()
# a =[[2, 4, 6, 8, 10, 12, 14, 16, 18],[1,3,5,7,9,12,13]]
# b = []
# for x in a:
#     for y in x:
#         if y % 3 != 0 or y % 7 != 0:
#             b.append(y)
# print(b)



#
# b= []
# for i in range(2,10):
#     a=[]
#     if i%3 !=0 and i%7 !=0:
#         for j in range(1,10):
#             if j%3 !=0 and j%7 !=0:
#                 a.append(i*j)
#             else:
#                 a +=[]
#     b.append(a)
# print(b)

# a = [1, 3, 11, 15, 23, 28, 37, 52, 85, 100]
# b = [ i for i in a if i % 2 == 0]
# print(b)


# a=[int(input()) for i in range(5)]
# print("입력된 값 %s의 평균은 "%str(a) +str(sum(a)/len(a))+"입니다.")

# a=input().split(',')
# a=list(map(int,a))
# print(a)
#
# def filly(a):
#     ac = []
#     for x in a:
#         if x % 3 != 0 or x % 5 !=0:
#             ac.append(x)
#     return ac
# b = filly(range(1, 21))
# c = [x**2 for x in b]
# print(c)

def calculat(a):
    return sum(a)

b = input()
print(type(b))
print(calculat(b))
