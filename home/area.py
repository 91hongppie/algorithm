import sys
sys.stdin = open('area.txt', 'r')
from collections import deque

def DFS(row, col):
    global result
    Q.append([row, col])
    while Q:
        a, b = Q.popleft()
        for k in range(4):
            x = a + dx[k]
            y = b + dy[k]
            if 0 <= x < r and 0 <= y < c:
                if board[x][y] == 0:
                    if visit[x][y] == False:
                        visit[x][y] = True
                        result += 1 
                        Q.append([x, y])
    
                    

r, c, nums = map(int, input().split())
board = [[0]*c for _ in range(r)]
result_list = []
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
for k in range(nums):
    c1, r1, c2, r2 = map(int, input().split())
    for i in range(r1, r2):
        for j in range(c1, c2):
            board[i][j] = 1
visit = [[False]*c for _ in range(r)]
for i in range(r):
    for j in range(c):
        if board[i][j] == 0:
            result = 0
            Q = deque()
            if visit[i][j] == False:
                DFS(i, j)
                if result == 0:
                    result += 1
                result_list.append(result)
result_list.sort()
print(len(result_list))
print(*result_list)