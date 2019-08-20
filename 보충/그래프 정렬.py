def DFS(v):
    visit[v] = True
    for w in G[v]:
        if not visit[w]:
            DFS(w) 




# -------------------------------------------
import sys
sys.stdin = open('sample_input_03.txt', 'r')

N = int(input())

for i in range(1, N+1):
    V, E = map(int, input().split())
    G = [[] for _ in range(V+1)]
    visit = [False for _ in range(V+1)]
    for j in range(E):
        u, v = map(int, input().split())
        G[u].append(v)
    s, e = map(int, input().split())
    DFS(s)
    if visit[e] == True:
        print('#{} 1'.format(i))
    else:
        print('#{} 0'.format(i))
