'''
1 1 1 1 1
1 0 0 0 1
1 0 0 0 1
1 0 0 0 1
1 1 1 1 1
정답 24
'''

# def isWall(x, y): #벽을 확인하고 아니면 진행
#     if x < 0 or x > 5: return True
#     if y < 0 or y > 5: return True
#     return False
#
# def calAbs(y, x): #벽이 아닐시 확인된 값의 반환 과정에서 음수일 경우르 대비해 절대값으로 계산
#     if y - x > 0: return y - x
#     else: return -(y-x)
#
# arr = [[0 for _ in range(5)] for _ in range(5)] #초기화 값을 조정, 불필요한 변수 저장을 위해 _ 기호 사용
# for i in range(5):
#     arr[i] = list(map(int, input().split()))
#
# dx = [0,0,-1,1]
# dy = [-1,1,0,0]
# sum = 0
# for x in range(len(arr)):
#     for y in range(len(arr[x])):
#         for i in range(4):
#             testX = x + dy[i]
#             testY = y + day[i]
#             if isWall(testX, testY) == False:
#                 sum += calAbs(arr[y][x], arr[testY, testX])


#전치 배열

# i : 행의 좌표, len(arr)
# j : 열의 좌표, len(arr[0])
# arr = [[1,2,3], [4,5,6], [7,8,9]] #3x3 행렬

# for i in range(3):
#     for j in range(3):
#         if i < j:
#             arr[i][j], arr[j][i] = arr[j][i], arr[i][j]
#
# for i in range(len(arr)):
#     for j in range(len(arr[i])):
#         print(arr[i][j], end=' ')
#     print()


# def printList(data, bit):
#    for i in range(len(bit)):
#        if bit[i]: print(data[i], end=" ")
#    print()
#
# data = [1,2,3]
# bit = [0, 0, 0, 0]
# for i in range(2):
#     bit[0] = i
#     for j in range(2):
#         bit[1] = j
#         for k in range(2):
#             bit[2] = k
#             for l in range(2):
#                 bit[3] = l
#                 print(data, bit)

# arr = [1,2,3]
# n = len(arr)
#
# for i in range(1 << n):
#     for j in range(n):
#         if i & (1<<j):
#             print(arr[j], end=',')
#     print()

# sum = 0
# arr = list(map(int,input().split()))
# for i in range(1, 1<<len(arr)):
#     sum = 0
#     for j in range(len(arr)):
#         if i & (1 << j): sum += arr[j]
#
#     if sum == 10:
#         for j in range(len(arr)):
#             if i & (i<< j):
#                 print(arr[j], end=" ")
#         print()

# def sequentialSearch(a,n,key):
#     i = 0
#     while i < n and a[i] != key:
#         i += 1
#
#     if i < n : return i
#     else: return -1
#
# data = [4, 9, 11, 23, 2, 19, 7]
# key = 19
# print(sequentialSearch(data, len(data), key))

# import bisect
#
# data = [2,4,7,9,11,19,23]
# print(bisect.bisect(data, 19))
#
# def binarySearch(a, key):
#     start = 0
#     end = len(a) - 1
#     while start <= end:
#         middle = (start + end) // 2
#         if key == a[middle]:
#             return middle
#         elif key < a[middle]:
#             end = middle - 1
#         else:
#             start = middle + 1
#     return -1
#
# key = 19
# data = [2,4,7,9,11,19,23]
# print(binarySearch(data, key))

def selectionSort(a):
    for i in range(0, len(a)-1):
        min = i
        for j in range(i + 1, len(a)):
            if a[min] > a[j]:
                min = j
        a[i], a[min] = a[min], a[i]

data = [3, 99, 23, 5, 32, 521, 56, 691, 97]
selectionSort(data)
print(data)