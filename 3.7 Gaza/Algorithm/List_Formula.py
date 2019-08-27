for i in range(len(data)):
    for j in range(len(data[i])):
        print(data[i][j], end=" ")
    print()
print()
#리스트가 들어와있는 표를 확인할 수 있는 공식
# 2차원 리스트 생성
depth_lists = [[0 for col in range(10)] for row in range(10)]