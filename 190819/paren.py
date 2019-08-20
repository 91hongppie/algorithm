import sys
sys.stdin = open('sample_input_paren.txt', 'r')

N = int(input())

for i in range(1, N+1):
    result = []
    S = input()
    for j in S:
        if j in '({':
            result.append(j)
        elif j == ')':
            if result[-1] == '(':
                result.pop()
            elif result[-1] != '(' or len(result) == 0:
                print('#{} 0'.format(i))
                break
        elif j == '}':
            if result[-1] =='{':
                result.pop()
            elif result[-1] != '{' or len(result) == 0:
                print('#{} 0'.format(i))
                break
    if len(result) == 0:
        print('#{} 1'.format(i))
    else:
        print('#{} 0'.format(i))
        

