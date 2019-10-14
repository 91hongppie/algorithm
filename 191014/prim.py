V, E = map(int, input().split())
G = [[] for _ in range(V)]  # 0 ~ V - 1
for _ in range(E):
    u, v, w = map(int, input().split())
    G[u].append((v, w))
    G[v].append((u, w))

key = [0xfffff] * V
pi = [-1] * V   # -1 => NULL(없다)
visit = [False] * V  # 트리에 포함된 정점들, 아닌 정점들 구분하기 위해서
key[0] = 0  # 시작점 0의 key 값 초기화
cnt = V
while cnt:  # 정점의 수 만큼 반복
    # key 값이 최소인 정점을 찾는다.
    u, MIN = 0, 0xfffff
    for i in range(V):
        if not visit[i] and MIN > key[i]:
            u, MIN = i, key[i]
    visit[u] = True
    # u의 인접정점을 찾아서 key, pi 를 변경
    for v, w in G[u]:
        if not visit[v] and w < key[v]:
            key[v] = w
            pi[v] = u

    cnt -= 1
