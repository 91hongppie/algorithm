import sys
sys.stdin = open('ladder_input.txt', 'r')

def DFS(row, col):
    if row == 0:
        print('#{} {}'.format(N, col))
        return
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    for i in range(4):
        x = row + dx[i]
        y = col + dy[i]
        if 0 <= x < 100 and  0 <= y < 100:
            if board[x][y] == 1:
                board[x][y] = 0
                break
    DFS(x, y)


for N in range(1, 11):
    n = int(input())
    board = []
    for _ in range(100):
        board.append(list(map(int, input().split())))
    s_point = board[99].index(2)
    DFS(99, s_point)