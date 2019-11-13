import sys
sys.stdin = open('mine.txt', 'r')
from pprint import pprint

def change(r, c):
    a = 0
    for k in range(8):
        x = r + dx[k]
        y = c + dy[k]
        if 0 <= x < rc and 0 <= y < rc:
            if board[x][y] == '*' or board[x][y] == -1:
                a += 1
    board[r][c] = a

def DFS(row, col):
    for y in range(8):
        x1 = row + dx[y]
        y1 = col + dy[y]
        if 0 <= x1 < rc and 0 <= y1 < rc:
            if not visit[x1][y1]:
                if board[x1][y1] == 0:
                    visit[x1][y1] = True
                    DFS(x1, y1)
                if board[row][col] == 0:
                    if not visit[x1][y1]:
                        visit[x1][y1] = True


N = int(input())

for tc in range(1, N+1):
    rc = int(input())
    dx = [0, 0, 1, -1, 1, -1, 1, -1]
    dy = [-1, 1, 0, 0, 1, -1, -1, 1]
    board = [list(map(str, input())) for _ in range(rc)]
    for i in range(rc):
        for j in range(rc):
            if board[i][j] == '*':
                board[i][j] = -1
            elif board[i][j] == '.':
                change(i, j)
    visit = [[False] * rc for _ in range(rc)]
    result = 0
    for k in range(rc):
        for u in range(rc):
            if board[k][u] != -1:
                if not visit[k][u]:
                    visit[k][u] = True
                    result +=1
                    DFS(k, u)
    print('#{} {}'.format(tc, result))
    