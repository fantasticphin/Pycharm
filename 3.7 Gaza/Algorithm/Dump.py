import sys
sys.stdin = open("Dump.txt")


for tc in range(1, 11):
    dump = int(input())
    inum = list(map(int,input().split()))

    for x in range(dump):
        minx = inum[0]
        maxx = inum[0]
        maxidx = 0
        minidx = 0
        for idx, i in enumerate(inum):
            if i > maxx:
                maxx = i
                maxidx = idx
            if i < minx:
                minx = i
                minidx = idx

        inum[maxidx] -= 1
        inum[minidx] += 1

    minx = inum[0] #초기변수를 다시 잡아줘서 max - min 을 할 수 있도록 셋팅해준다
    maxx = inum[0]
    maxidx = 0
    minidx = 0

    for idx, i in enumerate(inum):
        if i > maxx:
            maxx = i
            maxidx = idx
        if i < minx:
            minx = i
            minidx = idx

    result = maxx - minx

    print('#{} {}'.format(tc, result))

#은수님 풀이
    for test_case in range(1, 11):
        N = int(input())
        num = list(map(int, input().split()))
        for i in range(N):
            Max = 0
            Min = 100
            max_ind = 0
            min_ind = 0
            for comp_index in range(100):
                if num[comp_index] > Max:
                    Max = num[comp_index]
                    max_ind = comp_index
                if num[comp_index] < Min:
                    Min = num[comp_index]
                    min_ind = comp_index
            num[max_ind] -= 1
            num[min_ind] += 1
        Max = 0
        Min = 100
        for comp_index in range(100):
            if num[comp_index] > Max:
                Max = num[comp_index]
            if num[comp_index] < Min:
                Min = num[comp_index]
        print('#{} {}'.format(test_case, Max - Min))
