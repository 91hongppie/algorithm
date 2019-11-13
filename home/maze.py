import sys
sys.stdin = open('maze.txt', 'r')

def DFS(row, col):
    global result
    if board[row][col] == '3':
        result = 1
    if visit[row][col]==False:
        visit[row][col] = True
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for k in range(4):
        x = row + dx[k]
        y = col + dy[k]
        if 0<=x<16 and 0<=y<16:
            if visit[x][y]==False:
                if board[x][y] == '0' or board[x][y] == '3':
                    DFS(x, y)
for tc in range(1, 11):
    board = []
    result = 0
    i = int(input())
    visit = [[False]* 16 for _ in range(16)]
    for j in range(16):
        board.append(list(*map(str, input().split())))
        if '2' in board[j]:
            b = j
            c = board[j].index('2')

    DFS(b, c)
    print('#{} {}'.format(tc, result))