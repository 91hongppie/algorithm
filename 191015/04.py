from collections import deque
import sys
sys.stdin = open('04.txt', 'r')


def BFS(r, c, fuel):
    global result
    Q.append([r, c, fuel])
    while Q:
        x, y, gas = Q.popleft()
        if dp[x][y] == -1:
            dp[x][y] = gas
        elif dp[x][y] > gas:
            dp[x][y] = gas
        else:
            continue
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        for u in range(4):
            x1 = x + dx[u]
            y1 = y + dy[u]
            if 0 <= x1 < rc and 0 <= y1 < rc:


N = int(input())

for tc in range(1, N+1):
    rc = int(input())
    Q = deque()
    board = []
    result = 1e9
    dp = [[-1] * rc for _ in range(rc)]
    for _ in range(rc):
        board.append(list(map(int, input().split())))
    BFS(0, 0, 0)
    print('#{} {}'.format(tc, result))
