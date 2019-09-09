import sys
sys.stdin = open('wall_crash.txt', 'r')
from collections import deque

def BFS(s, e, cnt, dis):
    global result, check
    Q.append([s, e, cnt, dis])
    visit[s][e] = True
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    while Q:
        a = Q.popleft()
        for i in range(4):
            x1 = a[0]+dx[i]
            y1 = a[1]+dy[i]
            if 0 <= x1 < row and 0 <= y1 < col:
                # if not visit[x1][y1]:
                if room[x1][y1]:
                    if a[2] == 1:
                        visit[x1][y1] = True
                        Q.append([x1, y1, a[2]-1, a[3]+1])
                    else:
                        continue
                else:
                    visit[x1][y1] = True
                    Q.append([x1, y1, a[2], a[3]+1])
                    if x1 == row-1 and y1 == col-1:
                        result = min(result, a[3]+1)
                        check = 1



row, col = map(int, input().split())
room = [list(map(int, input())) for _ in range(row)]
visit = [[False]*col for _ in range(row)]
result = 500000
check = 0
Q = deque()
BFS(0, 0, 1, 1)
if check:
    print(result)
else:
    print(-1)