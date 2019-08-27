def find(data):
    for i in range(0,10):
        midx = i
        if i % 2 == 0:
            for j in range(i+1, N):
                if data[midx] < data[j]:
                    midx = j
        else:
            for j in range(i+1, N):
                if data[midx] > data[midx]:
                    midx = j

        data[i], data[midx] = data[midx], data[i] #구간의 합에 따라 바꿈

    return

T = int(input())

for t in range(1, T+1):
    N = int(input())
    data = list(map(int, input().split()))
    find(data)

    print('#P{'.format(t), end=" ")
    for i in range(10:
        print(data[i], end=" ")
    print())