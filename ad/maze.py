import sys; sys.stdin = open('maze.txt', 'r')
from queue import Queue

def BFS(sr, sc, cnt):
    global min_distance
    visit[sr][sc] = True
    Q.put([sr, sc, cnt])
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    while not Q.empty():
        a = Q.get()
        for y in range(4):
            if 0 <= a[1]+dx[y] < col and 0 <= a[0]+dy[y] < row:
                if room[a[0]+dy[y]][a[1]+dx[y]] == '1':
                    if a[0]+dy[y] == row-1 and a[1]+dx[y] == col-1:
                        min_distance = min(min_distance, a[2]+1)
                    elif not visit[a[0]+dy[y]][a[1]+dx[y]]:
                        visit[a[0]+dy[y]][a[1]+dx[y]] = True
                        Q.put([a[0]+dy[y], a[1]+dx[y], a[2]+1])






row, col = map(int, input().split())
room = [[] for _ in range(row)]
visit = [[False]*col for _ in range(row)]
for i in range(row):
    a = str(input())
    room[i].extend(a)
Q = Queue()
min_distance = 1e9
BFS(0, 0, 1)
print(min_distance)

