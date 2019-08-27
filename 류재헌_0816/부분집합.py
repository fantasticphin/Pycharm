import sys
sys.stdin = open('sub_set.text')

T = int(input())

for tc in range(T):
    # N = list(map(int, input().split()))
    data=[]
    for i in range(1,13):
        data.append(i)
    N,sum=(input().split())
    N=int(N)
    sum=int(sum)
    n = len(data)
    data_1=[]
    data_result=[]
    cnt=0

    for i in range(1<<n):# 부분집합 총원소를 구할거임
        for j in range(n+1):
            if i &(1<<j):
                data_1.append(data[j])
        data_result.append(data_1)
        data_1=[]
    # print(data_result) # 부분집합 원소를 데이터에 담음.
    for k in range(len(data_result)):
        if len(data_result[k])==N:
            sol = 0
            for z in range(N):
                sol+=data_result[k][z]
            if sol == sum:
                cnt+=1
    print(cnt)
