# def my_strrev(ary):
#     str = list(ary)
#     for i in range(len(str)//2):
#         t = ary[i]
#         str[i] = str[len(str)-1-i]
#         str[len(ary)-1-i] = t
#     ary = "".join(str)
#     return ary
#
# ary = "abcde"
# ary = my_strrev(ary)
# print(ary)

# s = "Reverse this strings"
# # s = s[-1:0:-1]
# print(s.reverse())
#

# def strcmp(str1, str2):
#     i = 0
#     if len(str1) != len(str2):
#         return False
#     else:
#         while i < len(str1) and i < len(str2):
#             if str1[i] != str2[i]:
#                 return False
#             i += 1
#     return True
#
# a = 'abc'
# b = 'abb'
#
# print(strcmp(a,b))

# print(str(123))
# print(repr(123))
# print(eval(str("12+3")))

# def atoi(string):
#     value = 0
#     i = 0
#     while (i < len(string)):
#         c = string[i]
#         if c >= '0' and c <='9':
#             digit = ord(c) - ord('9')
#         else:
#             break
#         value = (value * 10) + digit
#         i += 1
#     return value
#
# a = '123'
# print(type(a))
# b = atoi(a)
# print(type(b))
# c = int(a)
# print(type(c))

# def itoa(x):
#     strs = list()
#     count = 0
#     i, y = 0, 0
#     while True:
#         y = x % 10
#         strs.append(chr(y + ord('0')))
#         x //= 10
#         if x == 0: break
#         i += 1
#
#         strs.reverse()
#         strs = "".join(strs)
#     return strs
#
# x = 123
# print(x, type(x))
# str1 = itoa(x)
# print(str1, type(str1))


T = 'TTTTAACCA'
P = 'TTA'
M = len(P)
N = len(T)
def bruteforce(T, P):
    i = 0
    j = 0
    while j < M and i < N:
        if T[i] != P[j]:
            i = i - j
            j = -1
        i = i + 1
        j = j + 1
    if j == M : return i - M
    else : return -1

print(bruteforce(T, P))

def bfs2(t, p):
    for i in range(len(t) - len(p)+1):
        cnt = 0
        for j in range(len(p)):
            if t[i+j] != p[j]:
                break
            else:
                cnt += 1
        if(cnt >= len(p)) : return 1
    return -1

t ='TTTTAACCA'
p = 'TTA'
print('{}'.format(bruteforce(T,P)))
print('{}'.format(bfs2(t,p)))
print(t.find(p))