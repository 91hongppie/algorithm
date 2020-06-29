import sys
sys.stdin = open('cheese.txt', 'r')
sys.setrecursionlimit(10**4)
from collections import deque

def air(r, c):
    visit[r][c] = True
    Q.append([r, c])
    while Q:
        a, b = Q.popleft()
        for i in range(4):
            x = a + dx[i]
            y = b + dy[i]
            if 0 <= x < row and 0 <= y < col:
                if board[x][y] == 0 and visit[x][y] == 0:
                    visit[x][y] = 1
                    Q.append([x, y])

def cheese(r_x, c_y):
    for k in range(4):
        x1 = r_x + dx[k]
        y1 = c_y + dy[k]
        if 0 <= x1 < row and 0 <= y1 < col:
            if visit[x1][y1] == True:
                board[r_x][c_y] = 0
                return
        
row, col = map(int, input().split())
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
Q = deque()
board = [list(map(int, input().split())) for _ in range(row)]
num = -1
times = -1
result = 0
visit = [[0] * col for _ in range(row)]
while num != 0:
    air(0, 0)
    num = 0
    for st in range(row):
            num += sum(board[st])
    for i in range(1, row):
        for j in range(1, col):
            if board[i][j] == 1:
                cheese(i, j)
    for k in range(row):
        for h in range(col):
            visit[k][h] = 0
    if num != 0:
        result = num
    times += 1

print(times)
print(result)
