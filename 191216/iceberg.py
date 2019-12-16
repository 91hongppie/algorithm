import sys
sys.stdin = open('iceberg.txt', 'r')
from collections import deque

def bfs(row, col):
    Q.append([row, col])
    while Q:
        ro, co = Q.popleft()
        for o in range(4):
            x = ro + dx[o]
            y = co + dy[o]
            if 0 <= x < r and 0 <= y < c:
                if board[x][y] != 0:
                   if visit[x][y] == 0:
                       visit[x][y] = 1
                       Q.append([x, y])

def melt(row, col):
    global melt_list
    melt_volume = 0
    for k in range(4):
        x = row + dx[k]
        y = col + dy[k]
        if 0 <= x < r and 0 <= y < c:
            if board[x][y] == 0:
                melt_volume += 1
    melt_list.append([row, col, melt_volume])


dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
Q = deque()
r, c = map(int, input().split())
visit = [[0]*c for _ in range(r)]
board = [list(map(int, input().split())) for _ in range(r)]
island_nums = 0
for u in range(r):
    for y in range(c):
        if board[u][y] != 0:
            if visit[u][y] == 0:
                visit[u][y] = 1
                island_nums += 1
                bfs(u, y)
times = 0
while island_nums < 2:
    times += 1
    melt_list = []
    for i in range(r):
        for j in range(c):
            if board[i][j] != 0:
                melt(i, j)
    for k in melt_list:
        ice_row, ice_col, melt_volume = k[0], k[1], k[2]
        board[ice_row][ice_col] -= melt_volume
        if board[ice_row][ice_col] < 0:
            board[ice_row][ice_col] == 0
    island_nums = 0
    for u in range(r):
        for y in range(c):
            if board[u][y] != 0:
                if visit[u][y] == 0:
                    visit[u][y] = 1
                    island_nums += 1
                    bfs(u, y)
    for d in range(r):
        for b in range(c):
            visit[d][b] = 0
    result = 0
    for k in range(r):
        result += sum(board[k])
    if result == 0:
        times = 0
        break
print(times)