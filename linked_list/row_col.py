def BFS(table, r, c):
    global rc_list
    row = r
    col = c
    result_row = 1
    while table[row][col] != 0 and row < len(table):
        result_col = 1
        while table[row][col] != 0 and col < len(table):
            table[row][col] = 0
            result_col += 1
            col += 1
        row += 1
        col = c
        result_row += 1
    rc_list.append([result_row-1, result_col-1])


import sys
sys.stdin = open('input_row_col.txt', 'r')

N = int(input())

for i in range(1, N+1):
    rc = int(input())
    table = []
    for j in range(rc):
        table.append(list(map(int, input().split())))
    rc_list = []
    for r in range(rc):
        for c in range(rc):
            if table[r][c] != 0:
                BFS(table, r, c)
    rc_list = sorted(rc_list)
    for k in range(len(rc_list)):
        rc_list[k].insert(0, rc_list[k][0]*rc_list[k][1])
    print('#{} {}'.format(i, len(rc_list)), end=' ')
    for y in range(len(rc_list)-1):
        print('{} {}'.format(rc_list[y][1], rc_list[y][2]), end=' ')
    print('{} {}'.format(rc_list[-1][1], rc_list[-1][2]))

