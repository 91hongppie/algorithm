import sys
sys.stdin = open('num.txt', 'r')

def num(r, c, brick, cnt):
    global result
    if cnt == 6:
        result.add(brick)
        return
    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]
    for k in range(4):
        x = r + dx[k]
        y = c + dy[k]
        if 0 <= x < 4 and 0<= y <4:
            num(x, y, brick+board[x][y], cnt+1)

N = int(input())

for tc in range(1, N+1):
    result = set()
    board = []
    for _ in range(4):
        board.append(list(map(str, input().split())))
    for i in range(4):
        for j in range(4):
            br=board[i][j]
            num(i, j, br, 0)
    print('#{} {}'.format(tc, len(result)))