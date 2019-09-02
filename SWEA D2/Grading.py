import sys
sys.stdin = open('Grading.txt')

sco = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']
for t in range(int(input())):
    N,K = map(int,input().split())
    GR = [list(map(int,input().split()))for _ in range(N)]
    PT = []
    for x,y,z in GR:
        PT.append(x*35 + y*45 + z*20)
    K = PT[K-1]
    PT.sort(reverse=True)
    K = int(PT.index(K)/len(PT)*10)
    K = sco[K]
    print('#{} {}'.format(t+1, K))