import sys
sys.stdin = open('palindrome.txt')
# def palindrome(p, metrix):
#     cnt = 0
#     for row in metrix:
#         for i in range(8 - p + 1):
#             if row[i : i + p] == row[i : i + p][::-1]:
#                 cnt += 1
#     for col in zip(*metrix):
#         for i in range(8 - p + 1):
#             if ''.join(col)[i : i + p] == ''.join(col)[i : i + p][::-1]:
#                 cnt += 1
#     return cnt
# for t in range(1, 11):
#     p = int(input())
#     metrix = [input() for n in range(8)]
#     print('#{} {}'.format(t, palindrome(p, metrix)))



def palins(n, chart):
    cnt = 0
    for row in chart:
        for i in range(8 - n+1):
            if row[i : i + n] == row[i : i + n][::-1]:
                cnt += 1
    for colum in zip(*chart):
        for i in range( 8 - n+1):
            if "".join(colum)[i : i+n] == "".join(colum)[i : i+n][::-1]:
                cnt += 1
    return cnt

for T in range(1, 11):
    n = int(input())
    chart = [input() for x in range(8)]
    print('#{} {}'.format(T, palins(n, chart)))

#palindrome teacher
