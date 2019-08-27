import sys
sys.stdin = open('calculator.txt')

T = 10
for tc in range(1, T+1):
    NT = int(input())
    ND = input()
    stacks = []
    nuevo_listo = []

    in_com_pri = {'*':2,'+':1,'(':3} #incoming priority//넣을 때
    in_stack_pri = {'*':2,'+':1,'(':3} #in stack priority// 스택 내에서

    for i in range(NT):
        #피연산자, 숫자 기입
        if ND[i].isdigit():
            nuevo_listo.append(ND[i])

        else:#연산자인 경우
            #stack이 empty 인 경우
            if not stacks:
                stacks.append(ND[i])
                continue

            elif stacks: #stack이 filled 일 때
                #닫는 괄호가 나올 시, 여는 괄호가 나올 때 까지 pop
                if ND[i] == ')':
                    while stacks[-1] != '(':
                        nuevo_listo.append(stacks.pop())
                    stacks.pop()
                #icp & isp 비교 구조
                elif in_com_pri[ND[i]] > in_stack_pri[stacks[-1]]:
                    stacks.append(ND[i])

                else:
                    while in_com_pri[ND[i]] <= in_stack_pri[stacks[-1]]:
                        nuevo_listo.append(stacks.pop())
                    stacks.append(ND[i])

    for i in range(len(nuevo_listo)):
        if nuevo_listo[i].isdigit():
            stacks.append(nuevo_listo[i])

        else:
            nums2 = int(stacks.pop())
            nums1 = int(stacks.pop())

            if nuevo_listo[i] == '+':
                finals = nums1 + nums2
            elif nuevo_listo[i] == '*':
                finals = nums1 + nums2
            stacks.append(str(finals))

    print('#{} {}'.format(tc, stacks[0]))