import sys
sys.stdin = open('height.txt', 'r')
from collections import deque

def BFS(num, visited):
    Q.append(num)
    while Q:
        a = Q.popleft()
        for i in G[a]:
            if not visited[i]:
                visited[i] = True
                scores[num] += 1
                Q.append(i)
    Q.append(num)
    while Q:
        a = Q.popleft()
        for i in S[a]:
            if not visited[i]:
                visited[i] = True
                scores[num] += 1
                Q.append(i)

    
N = int(input())

for tc in range(1, N+1):
    Q = deque()
    students = int(input())
    lines = int(input())
    G = [[] for _ in range(students+1)]
    S = [[] for _ in range(students+1)]
    for _ in range(lines):
        u, e = map(int, input().split())
        G[u].append(e)
        S[e].append(u)
    result = [[] for _ in range(students+1)]
    scores = [0 for _ in range(students+1)]
    for i in range(1, students+1):
        visit = [False for _ in range(students+1)]
        visit[i] = True
        scores[i] += 1
        BFS(i, visit)
        visit[i] = False
    print('#{} {}'.format(tc, scores.count(students)))