import sys
sys.stdin = open('cell.txt', 'r')

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
N = int(input())
for tc in range(1, N+1):
    r, c, times = map(int, input().split())
    cells = [list(map(int, input().split())) for _ in range(r)]
    cells_dict = {}
    cells_list = []
    for i in range(r):
        for j in range(c):
            if cells[i][j] > 0:
                cells_dict[(i, j)] = (cells[i][j], cells[i][j])
                cells_list.append([i, j])
    i = 1
    while i < times:
        new_cells = {}
        for w, u in cells_dict.items():
            if i == u[1]:
                for h in range(4):
                    x = w[0] + dx[h]
                    y = w[1] + dy[h]
                    if [x, y] in cells_list:
                        continue
                    cells_list.append([x, y])
                    if (x, y) not in cells_dict:
                        new_cells[(x, y)] = (u[0], u[0]+u[1]+1)
                    else:
                        if u[0]+u[1]+1 > new_cells[(x, y)]:
                            new_cells[(x, y)] = (u[0], u[0]+u[1]+1)
        for p, s in new_cells.items():
            cells_dict[(p[0], p[1])] = s
        i += 1
    result = 0
    for u in cells_dict.values():
        if u[1] >= times:
            result += 1
    print(result)
            