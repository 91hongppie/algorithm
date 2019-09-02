import sys
sys.stdin = open('s_input.txt', 'r')

N = int(input())

for i in range(1, N+1):
    lines = int(input())
    line_list = []
    for j in range(lines):
        line_list.append(list(map(int, input().split())))
    terminals = int(input())
    terminal_list = []
    for k in range(terminals):
        terminal_list.append(int(input()))
    nums_list = [0] * 5001
    for u in line_list:
        for l in range(u[0], u[1]+1):
            nums_list[l] += 1
    print('#{}'.format(i), end=' ')
    for y in range(len(terminal_list)-1):
            print(nums_list[terminal_list[y]], end=' ')
    print(nums_list[terminal_list[-1]])

