import sys
sys.stdin=open('Node_Addition.txt')

for tc in range(1, int(input())+1):
    N,M,L = map(int,input().split())
    binary = [list(map(int,input().split()))for _ in range(M)]
    box = [0] * (N+2)
    # print(binary)
    for b in binary:
        box[b[0]] = box[1]
    for r in range(N,0,-1):
        if box[r]:
            continue
        box[r] = box[r*2] + box[r*2+1]
    print('#{} {}'.format(tc, box[L]))