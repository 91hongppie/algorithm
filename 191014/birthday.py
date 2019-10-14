from collections import deque
import sys
sys.stdin = open('birthday.txt', 'r')


def BFS(n):
    global cnt
    visit[n] = True
    Q.append([n, 0])
    while Q:
        a, b = Q.popleft()
        for k in G[a]:
            if visit[k] == False and b < 2:
                visit[k] = True
                Q.append([k, b+1])
                cnt += 1


N = int(input())

for tc in range(1, N+1):
    U, V = map(int, input().split())
    G = [[] for _ in range(U+1)]
    visit = [False for _ in range(U+1)]
    Q = deque()
    for i in range(V):
        u, v = map(int, input().split())
        G[u].append(v)
        G[v].append(u)
    cnt = 0
    BFS(1)
    print('#{} {}'.format(tc, cnt))
