import sys
sys.stdin = open('rain.txt', 'r')
from collections import deque

def bfs(x, y):
    Q.append([x, y])
    while Q:
        x1, y1 = Q.popleft()
        for h in range(4):
            x2 = x1 + dx[h]
            y2 = y1 + dy[h]
            if 0 <= x2 < rc and 0 <= y2 < rc:
                if visit[x2][y2] == 0:
                    Q.append([x2, y2])
                    visit[x2][y2] = 1


def rain_drop(rains):
    for x in range(rc):
        for y in range(rc):
            if board[x][y] <= rains:
                visit[x][y] = 1

rc = int(input())
Q = deque()
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
board = [list(map(int, input().split())) for _ in range(rc)]

max_num = 0
for i in range(rc):
    if max_num < max(board[i]):
        max_num = max(board[i])
visit = [[0] * rc for _ in range(rc)]
result = 1
for j in range(1, max_num+1):
    rain_drop(j)
    num = 0
    for r in range(rc):
        for c in range(rc):
            if visit[r][c] == 0:
                visit[r][c] = 1
                bfs(r, c)
                num += 1
    if result < num:
        result = num
    for u in range(rc):
        for z in range(rc):
            visit[u][z] = 0
print(result)
