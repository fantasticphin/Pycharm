'''
1~200 사이의 정수 가운데 7의 배수이면서 5의 배수는 아닌

b=0
a=''



for i in range(1,200):
    if (i%7)==0:
        if (i%5)!=0:

            if (b==0):
                b=b+1
                a=str(i)
            else:
                a+=","+str(i)
print(a)

100~300 사이의 숫자에서 각각의 자리 숫자가 짝수인 숫자를 찾아 콤마(,)로 구분해 출력하

a=''
b=0
for i in range(100, 300):
    if (int(i/100)%2==0):
        if (int(i / 10) % 2 == 0):
            if (int(i) % 2 == 0):
                if b==0:
                    b=1
                    a += str(i)
                else:
                    a+= ','+str(i)
print(a)
음의 결과와 같이 5명의 학생의 점수에 대해 60 이상일 때 합격 메시지를 출력하고,

60미만일 때 불합격 메시지를 출력하는 프로그램을 만드십시오.
a=[88,30,61,55,95]
for i in range(0,5):
    b=i+1
    if a[i]>=60:
        print("%d번 학생은 "%b+"%d점으로 합격입니다."%a[i])
    else:
        print("%d번 학생은 "%b+"%d점으로 불합격입니다."%a[i])
'''

# a=[85, 65, 77, 83, 75, 22, 98, 88, 38, 100]
# sum=0
# i=0
# while(i<len(a)):
#     if a[i]<80:
#         a.pop(i)
#     i=i+1
#
# for i in a[]:
#     sum+=a[i]
# print(sum)

a = 5
for i in range(a):
    for j in range(i):
        print('*', end="")
    print()
for x in range(a, 0, -1):
    for y in range(x):
        print('*', end='')
    print()