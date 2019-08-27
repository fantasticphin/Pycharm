import sys
sys.stdin = open('Doubledouble.txt')

T = int(input())
for i in range(T+1):
    result = 2**i
    print(result, end=' ')