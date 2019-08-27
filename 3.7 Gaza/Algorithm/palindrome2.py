import sys
sys.stdin = open('palindrome2.txt')
#

for rs in range(1, 11):
    input()
    l=[input()for res in range(100)]
    p=[[l[res][rej]for res in range(100)]for rej in range(100)]
    rests=1
    for i in range(2, 101):
        for j in range(101-i):
            for q in range(100):
                if l[q][j:j+i]==l[q][j:j+i][::-1] or p[q][j:j+i]==p[q][j:j+i][::-1]:rests=i
    print('#{} {}'.format(rs, rests))

# for rs in range(1, 11):
#     input();l=[input()for res in range(100)];p=[[l[res][rej]for res in range(100)]for rej in range(100)];rests=1
#     for i in range(2, 101):
#         for j in range(101-i):
#             for q in range(100):
#                 if l[q][j:j+i]==l[q][j:j+i][::-1] or p[q][j:j+i]==p[q][j:j+i][::-1]:rests=i
#     print('#{} {}'.format(rs, rests))