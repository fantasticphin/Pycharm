# def bit_print(i):
#     out = ''
#     for j in range(7,-1,-1):
#         out += '1' if i & (1 << j ) else '0'
#     print(out)
#
# for i in range(-5, 6):
#     print('%3d = ' % i, end='')
#     bit_print(i)


# arr = [0,0,0,0,0,0,0,1,1,1, 1,0,0,0,0,0,0,1,1,0, 0,0,0,0,0,1,1,1,1,0,
#        0,1,1,0,0,0,0,1,1,0, 0,0,0,1,1,1,1,0,0,1, 1,1,1,0,0,1,1,1,1,1,  1,0,0,1,1,0,0,1,1,1]
# for i in range(10):
#     n = 0
#     for j in range(i*7, i*7+7, 1):
#         n = n*2+arr[j]
#     print(n)

# arr = list(input())
# for i in arr:
#     if '0' < (arr[i]) < '9':
#         ord(arr[i]) - ord('0')
#     else:
#         ord(arr[i])-ord('A') + 10
# print(ord(arr[i]))

# a = len(bi) - (len(bi)//7*7)
# if len(bi) % 7 != 0:
#    n = 0
#    for j in range(len(bi)//7*7, len(bi),1):
#        n = n * 2 + bi[j]
#    print(n, end=" ")
# print()
asc = [[0,0,0,0],
       [0,0,0,1],
       [0,0,1,0],
       [0,0,1,1],
       [0,1,0,0],
       [0,1,0,1],
       [0,1,1,0],
       [0,1,1,1],
       [1,0,0,0],
       [1,0,0,1],
       [1,0,1,0],
       [1,0,1,1],
       [1,1,0,0],
       [1,1,0,1],
       [1,1,1,0],
       [1,1,1,1],
       ]
def aa(c):
    if c <= '9': return ord(c) - ord('0')
    else: return ord(c) - ord('A')+10

def at(x):
    for i in range(4):
        t.append(asc[x][i])
t = []
arr = input()
for i in range(len(arr)):
    at(aa(arr[i]))
n = 0
for i in range(len(t)):
    n = n*2+t[i]
    if i % 7 == 6:
        print(n, end=', ')
        n = 0

if i % 7 != 6:
    print(n)

# data = input()
# tmp = ''
# for i in data:
#    if '0' < i <= '9':
#        if len(bin(int(i))) == 3:
#            tmp += '000' + bin(int(i))[2::]
#        elif len(bin(int(i))) == 4:
#            tmp += '00' + bin(int(i))[2::]
#        elif len(bin(int(i))) == 5:
#            tmp += '0' + bin(int(i))[2::]
#        else:
#            tmp += bin(int(i))[2::]
#    else:
#        tmp += bin(int(ord(i)))[2::] - bin(int(ord('A'))) + 10
# print(tmp)
# for i in range(0, len(tmp), 7):
#    print(int(tmp[i: i+7], 2))