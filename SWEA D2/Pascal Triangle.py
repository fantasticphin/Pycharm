import sys
sys.stdin = open('Pascal.txt')

for t in range(int(input())):
    N = int(input())
    pascal = [[0 for j in range(i+3)]for i in range(N)] #파스칼 제작
    pascal[0][1] = 1 #가변 1
    for i in range(1,N): #파스칼 삼각형의 열 제작
        for j in range(i+1): #파스칼 삼각형 행 제작
            pascal[i][j+1] = pascal[i-1][j] + pascal[i-1][j+1] #기입될 수는 왼쪽 위와 오른쪽의 합
    print('#{}'.format(t+1))
    for k in pascal:
        print(' '.join(list(map(str,k[1:-1])))) #리스트를 0으로 초기값을 잡고 시작, 각 끝의 0 제거 후 출력
