import sys
sys.stdin = open('RGB.txt', 'r')
sys.setrecursionlimit(10**9)


def DFS(r, c, col):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    visit[r][c] = True
    for k in range(4):
        x1 = r + dx[k]
        y1 = c + dy[k]
        if 0 <= x1 < N and 0 <= y1 < N:
            if visit[x1][y1] == False:
                if board[x1][y1] == col:
                    visit[x1][y1] = True
                    DFS(x1, y1, col)


def DFS1(r, c, col):
    global board
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    visit1[r][c] = True
    for k in range(4):
        x1 = r + dx[k]
        y1 = c + dy[k]
        if 0 <= x1 < N and 0 <= y1 < N:
            if visit1[x1][y1] == False:
                if col == 'R' or col == 'G':
                    if board[x1][y1] == 'R' or board[x1][y1] == 'G':
                        visit1[x1][y1] = True
                        DFS1(x1, y1, col)
                else:
                    if board[x1][y1] == col:
                        visit1[x1][y1] = True
                        DFS1(x1, y1, col)



N = int(input())
board = []
visit = [[False]*N for _ in range(N)]
visit1 = [[False]*N for _ in range(N)]
result = result1 = 0
for _ in range(N):
    board.append(list(map(str, input())))

for i in range(N):
    for j in range(N):
        if not visit[i][j]:
            DFS(i, j, board[i][j])
            result += 1
        if not visit1[i][j]:
            DFS1(i, j, board[i][j])
            result1 += 1
print('{} {}'.format(result, result1))
