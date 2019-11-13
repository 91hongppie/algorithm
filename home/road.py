import sys
sys.stdin = open('road.txt', 'r')
from collections import deque

def DFS(s):
    global result_list
    Q.append(s)
    while Q:
        a = Q.popleft()
        for y in G[a]:
            if result_list[s][y] == 0:
                result_list[s][y] = 1
                Q.append(y)
            else:
                continue



N = int(input())
board = []
G = [[] for _ in range(N)]
for _ in range(N):
    board.append(list(map(int, input().split())))
for i in range(N):
    for j in range(N):
        if board[i][j] == 1:
            G[i].append(j)
result_list = [[0]*N for _ in range(N)]
Q = deque()
for k in range(N):
    DFS(k)         
for h in range(N):
    print(*result_list[h])