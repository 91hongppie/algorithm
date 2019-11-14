import sys
sys.stdin = open('prison.txt', 'r')
from pprint import pprint
def DFS(r, c, t):
    global result
    if t == T:
        return
    if board[r][c] == 1:
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        for h in range(4):
            x = r + dx[h]
            y = c + dy[h]
            if 0 <= x < H and 0 <= y < W:
                if board[x][y] != 0:
                    if visit[x][y] == 0:
                        visit[x][y] = 1
                        DFS(x, y, t+1)
    elif board[r][c] == 2:
        dy = [-1, 1]
        for h in range(2):
            x = r + dy[h]
            y = c 
            if 0 <= y < W:
                if board[x][y] != 0:
                    if visit[x][y] == 0:
                        visit[x][y] = 1
                        DFS(x, y, t+1)
    elif board[r][c] == 3:
        dx = [-1, 1]
        for h in range(2):
            x = r 
            y = c + dx[h]
            if 0 <= y < W:
                if board[x][y] != 0:
                    if visit[x][y] == 0:
                        visit[x][y] = 1
                        DFS(x, y, t+1)
    elif board[r][c] == 4:
        if c+1 < W:
            if board[r][c+1] != 0:
                if visit[r][c+1] == 0:
                    visit[r][c+1] = 1
                    DFS(r, c+1, t+1)
    elif board[r][c] == 5:
        if 0 <= c-1:
            if board[r][c-1] != 0:
                if visit[r][c-1] == 0:
                    visit[r][c-1] = 1
                    DFS(r, c-1, t+1)
    elif board[r][c] == 6:
        if r + 1 < H:
            if board[r+1][c] != 0:
                if visit[r+1][c] == 0:
                    visit[r+1][c] = 1
                    DFS(r+1, c, t+1)
    elif board[r][c] == 7:
        if 0 <= r - 1:
            if board[r-1][c] != 0:
                if visit[r-1][c] == 0:
                    visit[r-1][c] = 1
                    DFS(r-1, c, t+1)
   



N = int(input())
for tc in range(1, N+1):
    result = 0 
    H, W, M_H, M_W, T = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(H)]
    visit = [[0] * W for _ in range(H)]
    visit[M_H][M_W] = 1
    DFS(M_H, M_W, 1)
    for i in range(H):
        for j in range(W):
            if visit[i][j] == 1:
                result += 1
    print(result)
    print('#{} {}'.format(tc, result))
    for y in range(H):
        print(visit[y])