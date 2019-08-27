import sys
sys.stdin = open('N_addition.txt')

def addis(n):
    return int(n*(n+1)/2)

T = int(input())

print(addis(26))
