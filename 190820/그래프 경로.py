def DFS(v):
    stack = []
    stack.append(v)
    visit[v] = True

    while len(stack) > 0:
        prev = v
        for w in G[v]:
            if not visit[w]:
                stack.append(w)
                v = w
                visit[w] = True
                break
        if prev == v:
            v = stack.pop()
        if v == e:
            print('#{} 1'.format(i))
            break
    else:
        print('#{} 0'.format(i))


# ---------------
import sys
sys.stdin = open('sample_input_03.txt', 'r')

N = int(input())

for i in range(1, N+1):
    V, E = map(int, input().split())
    G = [[] for _ in range(V + 1)]
    visit = [False for _ in range(V + 1)]
    for k in range(E):
        u, v = map(int, input().split())
        G[u].append(v)
    s, e = map(int, input().split())
    DFS(s)