import sys
sys.stdin = open("Card_sample.txt")
#
T = int(input())

for x in range(1, T+1):
    counts = [0] * 10 #카드를 셀 수 있는 빈 칸을 만들어 줌
    N = int(input()) # 카드 개수
    data = input() # 들어온 카드
    for k in data: #data 내에 있는 요소들을 반복문으로 끄집어냄
        counts[int(k)] += 1 #data 내에서 추출된 각 요소마다 요소의 해당 수에 위치하는 곳에 배치 후 +1
    for idx,j in enumerate(counts): #모든 요소가 정리된 후, counts 요소가 채워짐
        if max(counts)==j: #카운트 배열 내에 맥스 함수를 통해 j 와 동일하면
            max_index=idx  #최대값과 자리숫를 출력
    print('# {} {} {}'.format(x,max_index,max(counts)))

    #num = [4,9,6,7]
    # num % 10 #10으로 나누면 뒷자리수인 7만 나오게 됨
    # num // = 10 #496 을 10으로 나눈 몫 값을 저장
    #list 는 참조형 즉, 주소값을 가지고 있다. 변수와 다름