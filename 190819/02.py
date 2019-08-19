import sys
sys.stdin = open('sample_input_01.txt', 'r')

N = int(input())

for i in range(1, N+1):
    S_list = []
    S = input()
    for j in S:
        if j == '(':
            S_list.append(j)
        elif j == ')':
            if S_list[-1] == '(':
                S_list.pop()
            elif len(S_list) == 0:
                print('#{} 0'.format(i)) 
                break
        if j == '{':
            S_list.append(j)
        elif j == '}':
            if S_list[-1] == '{':
                S_list.pop()
            elif len(S_list) == 0:
                print('#{} 0'.format(i))
                break
    else:
        print('#{} 1'.format(i))