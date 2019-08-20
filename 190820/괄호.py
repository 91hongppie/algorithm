import sys
sys.stdin = open('sample_input_02.txt', 'r')

N = int(input())

for i in range(1, N+1):
    sen = input()
    paren_list = []
    for idx, k in enumerate(sen):
        if k == '(':
            paren_list.append(k)
        elif k == ')':
            if len(paren_list) == 0 or paren_list[-1] != '(':
                print('#{} 0'.format(i))
                break
            elif paren_list[-1] == '(':
                paren_list.pop()
        elif k == '{':
            paren_list.append(k)
        elif k == '}':
            if len(paren_list) == 0 or paren_list[-1] != '{':
                print('#{} 0'.format(i))
                break
            elif paren_list[-1] == '{':
                paren_list.pop()
        if idx == len(sen)-1:
            if len(paren_list) == 0:
                print('#{} 1'.format(i))
            else:
                print('#{} 0'.format(i))
