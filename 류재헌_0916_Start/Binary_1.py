import sys
sys.stdin = open('Binary_1.txt')
Binaries = ['0000',
            '0001',
            '0010',
            '0011',
            '0100',
            '0101',
            '0110',
            '0111',
            '1000',
            '1001',
            '1010',
            '1011',
            '1100',
            '1101',
            '1110',
            '1111']

for tc in range(1,int(input())+1):
    N,No = input().split()

    check = ''
    for n in No:
        if n == 'A':
            check += Binaries[10]
        elif n == 'B':
            check += Binaries[11]
        elif n == 'C':
            check += Binaries[12]
        elif n == 'D':
            check += Binaries[13]
        elif n == 'E':
            check += Binaries[14]
        elif n == 'F':
            check += Binaries[15]
        else:
            check += Binaries[int(n)]

    print('#{} {}'.format(tc, check))