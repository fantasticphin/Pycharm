# input
# a = input()
# print(a)

#('1', '2', '3') <= 튜플/tuple 자료
#divmod
# a = 10
# b = 32
# c = divmod(b,a)
# print(c)

#map
# a = [1,2,4,5,3,5]
# def b(k):
#     return k*2
# c = list(map(b,a))
# print(c)

# #홀짞 구분
# number = int(input('Enter_Number :'))
# if number%2 == 0:
#     print('짝')
# else:
#     print('홀')

# 첫글자와 끝글자 구분해내는 프로그램
# str = input('문자를 입력하세요 :')
# print(str[:1], str[-1:])
# print(f'첫 글자는 {str[0]}입니다.')
# print(f'마지막 글자는 {str[-1]} 입니다.')

#자연수 n 으로 한 줄에 하나씩 출력
# n = int(input('숫자를 입력하세요 : '))
# i = 0
# for i in range(n):
#     print(i +1)

# for i in range(5):
#     print('{:>5}'.format('*' * (i+1)))

#10진수를 2진수로 변환
# print(bin(int(input()))[2:])

# student = {'python' : 80, 'algorithm': 99, 'django': 89, 'flask': 83}
# avg = sum((student.values()) / len(student.values))

# def ssafy(name, location='서울'):
#     print('{}의 지역은 {}입니다.'.format(name, location))
# print(ssafy(name='허준', '구미'))

# def my_func(a,b):
# 	c = a + b
# 	print(c)
# print(my_func(4,7))

# dir(__builtins__)
# print(dir(__builtins__))

# def palindrome(a):
# #     if a == a[::-1]:
# #         return True
# #     else:
# #         return False
# # print(palindrome('level'))

a = int(input())
def decimal():
    for i in a:
        if i == True:
            print('정수입니다.')
    else:
        print('소수입니다.')

print(decimal(13))
