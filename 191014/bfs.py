from collections import deque

V, E = map(int, input().split())
G = [[] for _ in range(V + 1)]  # 1 ~ V
for _ in range(E):
    u, v, w = map(int, input().split())
    G[u].append((v, w))
    G[v].append((u, w))


def BFS(s):
    Q = deque()
    D = [0xfffffff] * (V + 1)   # D[] 배열 초기값 설정
    D[s] = 0    # 출발점의 D 값을 0으로 설정
    Q.append(s)
    while Q:
        u = Q.popleft()
        for v, w in G[u]:
            if D[v] > D[u] + w:
                D[v] = D[u] + w
                Q.append(v)


BFS(1)
