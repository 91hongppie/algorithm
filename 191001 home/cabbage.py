import sys
sys.stdin = open('cabbage.txt', 'r')
from collections import deque
def BFS(y, u):
    Q.append([y, u])
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    while Q:
        x, y = Q.popleft()
        for i in range(4):
            x1 = x + dx[i]
            y1 = y + dy[i]
            if 0 <= x1 < r and 0 <= y1 < c:
                if board[x1][y1] == 1:
                    board[x1][y1] = 0
                    Q.append([x1, y1])


N = int(input())

for tc in range(1, N+1):
    r, c, nums = map(int, input().split())
    board = [[0]*c for _ in range(r)]
    for _ in range(nums):
        a, b = map(int, input().split())
        board[a][b] = 1
    Q = deque()
    count = 0
    for i in range(r):
        for j in range(c):
            if board[i][j] == 1:
                board[i][j] = 0
                BFS(i, j)
                count += 1
    print(count)
