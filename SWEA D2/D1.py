# ss = 'python'
#
# for i in range(0,6) :
#
#     print(ss[i]+'$',end='')

# n = input()+','
# n=sorted(n.split())
# n=' '.join(n)
# print(n[:-1])
#6297
# n = input()
# b = list(n.split(', '))
# c = [s for i,s in enumerate(b) if (i+1) % 2]
# print(', '.join(c))

#6298
# a = (1,2,3,4,5,6,7,8,9,10)
# b = a[:5]
# c = a[5:]
# print(b)
# print(c)

#6299
# a = [5, 6, 77, 45, 22, 12, 24]
# b = [i for i in a if i % 2 != 0]
# print(b)

#6300
# a = [12, 24, 35, 70, 88, 120, 155]
# b = []
# for i in range(1,6,2):
#     b.append(a[i])
# print(b)

#6301
# a = [[[0 for col in range(4)] for row in range(3)] for depth in range(2)]
# print(a)

#6302
# a = [12, 24, 35, 70, 88, 120, 155]
# a.remove(a[0])
# a.remove(a[3])
# a.remove(a[3])
# print(a)

#6303
# a = [1,3,6,78,35,55]
# b = [12,24,35,24,88,120,155]
# c = []
# for x in b:
#     if x in a:
#         c.append(x)
# print(c)

# #6305
# a = [12,24,35,24,88,120,155,88,120,155]
# aa = sorted(set(a))
# print(aa)

# 6254
# stu = {'홍길동':'010-1111-1111','이순신':'010-1111-2222','강감찬':'010-1111-3333'}
# a = input()
# print('아래 학생들의 전화번호를 조회할 수 있습니다.\n홍길동\n이순신\n강감찬\n전화번호를 조회하고자 하는 학생의 이름을 입력하십시오.\n이순신의 전화번호는 {}입니다.'.format(stu.get(a)))

#6255
product = {
"TV": 2000000,

"냉장고": 1500000,

"책상": 350000,

"노트북": 1200000,

"가스레인지": 200000,

"세탁기": 1000000,

}

products = sorted(product.items(), key=lambda t : t[1])
print(products)