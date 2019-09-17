import sys
sys.stdin = open('Binary_Passcode2.txt')

for tc in range(1, int(input())+1):
    N,M = map(int,input().split())
    dax = [list(map(input().split()))for _ in range(M)]
    print(dax)