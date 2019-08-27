import sys
sys.stdin = open('sample_forth.txt', 'r')

N = int(input())
for i in range(1, N+1):
    num_list = list(input().split())
    stack = []
    oper = []
    for j in range(len(num_list)):
        if num_list[j].isdigit():
            stack.append(num_list[j])
        elif num_list[j] == '.':
            if len(stack) == 1 and len(oper) == 0:
                print('#{} {}'.format(i, stack[0]))
            else:
                print('#{} error'.format(i))
        else:
            oper.append(num_list[j])
            if len(stack) > 1:
                b = int(stack.pop())
                a = int(stack.pop())
                c = oper.pop(0)
                if c == '+':
                    calc = a + b
                elif c == '-':
                    calc = a - b
                elif c == '*':
                    calc = a * b
                elif c == '/':
                    calc = a / b
                stack.append(int(calc))
            else:
                print('#{} error'.format(i))
                break
                


    