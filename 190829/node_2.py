def BFS(f, l, c):
    Q.append([f, c])
    if f == l:
        print('#{} {}'.format(i, c))
        return
    while Q:
        print(Q)
        a = Q.pop(0)
        visit[a[0]] = True
        if a[0] == l:
            print('#{} {}'.format(i, a[1]))
            return
        else:
            for k in G[a[0]]:
                if not visit[k]:
                    visit[k] = True
                    Q.append([k, a[1]+1])
                
            

import sys
sys.stdin = open('sample_node.txt', 'r')

N = int(input())

for i in range(1, N+1):
    V, E = map(int, input().split())
    G = [[] for _ in range(V+1)]
    visit = [False for _ in range(V+1)]
    for j in range(E):
        v, e = map(int, input().split())
        G[v].append(e)
        G[e].append(v)
    s, e = map(int, input().split())
    Q = []
    print(G)
    BFS(s, e, 0)
