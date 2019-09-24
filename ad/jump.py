import sys
sys.stdin = open('jump.txt', 'r')


def DFS(r, c, result):
    if len(result) == 6:
        a = ''.join(result)
        if a in baam:
            return
        baam.append(a)
        return
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    for u in range(4):
        x = r + dx[u]
        y = c + dy[u]
        if 0 <= x < len(board) and 0 <= y < len(board):
            result.append(board[x][y])
            DFS(x, y, result)
            result.pop()


board = []
for _ in range(5):
    board.append(list(map(str, input().split())))
result = []
baam = []
for i in range(5):
    for j in range(5):
        result.append(board[i][j])
        DFS(i, j, result)
        result.pop()
print(len(baam))
