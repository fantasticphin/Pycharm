import sys
sys.stdin = open('input.txt')
T = int(input())
r,c = map(int,input().split(''))
data = [list(map(int,input()))for _ in range(r)]

print(T)
print(str(r)+''+str(c))
for i in range(r):
    for j in range(c):
        print(data[i][j], end='')
    print()