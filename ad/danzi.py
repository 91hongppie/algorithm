import sys
sys.stdin = open('danzi.txt', 'r')
from collections import deque

def BFS(r, c):
    global count
    visit[r][c] = True
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    Q.append([r, c])
    result = 1
    while Q:
        a = Q.popleft()
        for k in range(4):
            if 0 <= a[0]+dy[k] < N and 0 <= a[1]+dx[k] < N:
                if room[a[0]+dy[k]][a[1]+dx[k]] == 1:
                    if not visit[a[0]+dy[k]][a[1]+dx[k]]:
                        Q.append([a[0]+dy[k], a[1]+dx[k]])
                        visit[a[0]+dy[k]][a[1]+dx[k]] = True
                        result += 1
    result_list.append(result)
    count += 1



N = int(input())
room = [list(map(int, input())) for _ in range(N)]
visit = [[False]*N for _ in range(N)]
Q = deque()
count = 0
result_list = []
for r in range(len(room)):
    for c in range(len(room)):
        if visit[r][c] == False and room[r][c] == 1 :
            BFS(r, c)
result_list.sort()
print(count)
for you in result_list:
    print(you)
