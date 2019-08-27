import sys
sys.stdin = open('duplicate_deletion.txt')

TC = int(input())

for tc in range(1, TC+1):
    data = list(input());nos = len(data);stk = []
    for i in range(nos): #stack 공백 여부 확인,
        if not stk or stk[-1] != data[i]:
            stk.append(data[i])
        elif stk and stk[-1] == data[i]: #stack 값 확인 후 내 값과 동일 확인
            stk.pop()
    print('#{} {}'.format(tc, len(stk)))