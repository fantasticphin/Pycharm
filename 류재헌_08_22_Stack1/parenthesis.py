import sys
sys.stdin = open ('parenthesis.txt')

T = int(input())

for tc in range(1, T+1):
    DT = input();N = len(DT);stk = []
    for i in range(N):
        if DT[i] =='(' or DT[i] == '{':
            stk.append(DT[i])
        elif DT[i] == ')' or DT[i] == '}':
            if len(stk) == 0:
                stk = [DT[i]]
                break
            elif (DT[i] == '}' and stk[-1] != '{') or (DT[i] == ')' and stk[-1] != '}'):
                stk = DT[i]
                break
            else:
                stk.pop()

    if not len(stk):
        print('#{} 1'.format(tc))
    else:
        print('#{} 0'.format(tc))