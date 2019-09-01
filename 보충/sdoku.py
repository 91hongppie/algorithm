import sys
sys.stdin = open('input_sdoku.txt', 'r')

N = int(input())

for i in range(1, N+1):
    sdoku_list = []
    result = 0
    for _ in range(9):
        sdoku_list.append(list(map(int, input().split())))
    for e in range(9):
        if len(sdoku_list[e]) == len(set(sdoku_list[e])):
            result += 1
    for r in range(9):
        col_list = []
        for c in range(9):
            col_list.append(sdoku_list[c][r])
        if len(col_list) == len(set(col_list)):
            result += 1
    for k in range(0, 9, 3):
        for u in range(0, 9, 3):
            part_list = []
            for v in range(3):
                for x in range(3):
                    part_list.append(sdoku_list[k+v][u+x])
            if len(part_list) == len(set(part_list)):
                result += 1

    if result != 27:
        print('#{} 0'.format(i))
    else:
        print('#{} 1'.format(i))

        
