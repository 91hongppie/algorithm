from pprint import pprint
import sys
sys.stdin = open('02.txt', 'r')


def navi(num, r, c, cnt):
    global result
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    i, j, a, h = r, c, cnt, num
    while True:
        if dp[h]:
            dp[h-1] = dp[h] + 1
            return
        for k in range(4):
            x = i + dx[k]
            y = j + dy[k]
            if 0 <= x < rc and 0 <= y < rc:
                if board[x][y] == h+1:

                    i = x
                    j = y
                    a += 1
                    h += 1
                    break
        if i != x or j != y:
            break
    for y in range(num, h+1):
        dp[y] = a
        a -= 1


N = int(input())
for tc in range(1, N+1):
    rc = int(input())
    board = []
    for _ in range(rc):
        board.append(list(map(int, input().split())))
    dp = [0 for _ in range(rc**2+1)]
    for i in range(rc):
        for j in range(rc):
            if not dp[board[i][j]]:
                result = 0
                navi(board[i][j], i, j, 1)
    a, b, = 0, 1e9
    for idx, val in enumerate(dp):
        if val > a:
            b = idx
            a = val
    print('#{} {} {}'.format(tc, b, a))
