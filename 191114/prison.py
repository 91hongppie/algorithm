import sys
sys.stdin = open('prison.txt', 'r')
from pprint import pprint
from collections import deque

IN = [[1, 2, 5, 6], [1, 2, 4, 7], [1, 3, 4, 5], [1, 3, 6, 7]]
OUT = [[1, 2, 4, 7], [1, 2, 5, 6], [1, 3, 6, 7], [1, 3, 4, 5]]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def BFS(r, c):
    Q.append([r, c, 1])
    while Q:
        a, b, t = Q.popleft()
        if t == T:
            return
        for i in range(4):
            if board[a][b] not in OUT[i]:
                continue
            x = a + dx[i]
            y = b + dy[i]
            if 0 <= x < H and 0 <= y < W:
                if board[x][y] not in IN[i]:
                    continue
                else:
                    if visit[x][y] == 0:
                        visit[x][y] = 1
                        Q.append([x, y, t+1])

N = int(input())
for tc in range(1, N+1):
    Q = deque()
    result = 0
    H, W, m_r, m_c, T = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(H)]
    visit = [[0]*W for _ in range(H)]
    visit[m_r][m_c] = 1
    BFS(m_r, m_c)
    for k in range(H):
        result += visit[k].count(1)
    print('#{} {}'.format(tc, result))