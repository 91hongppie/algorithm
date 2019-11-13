import sys
sys.stdin = open('virus.txt', 'r')
from collections import deque
def BFS(num):
    global result
    visit[num] = True
    Q.append(num)
    while Q:
        a = Q.popleft()
        for u in G[a]:
            if visit[u] == False:
                result += 1
                visit[u] =True
                Q.append(u)

computers = int(input())
Q = deque()
result = 0
visit = [False for _ in range(computers+1)]
G = [[] for _ in range(computers+1)]
lines = int(input())
for i in range(lines):
    u, e = map(int, input().split())
    G[u].append(e)
    G[e].append(u)
BFS(1)
print(result)