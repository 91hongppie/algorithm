def DFS(v):
    stack = []
    stack.append(v)
    visit[v] = 1

    while len(stack) > 0:
        prev = v
        for w in G[v]:
            if not visit[w]:
                stack.append(w)
                v = w
                visit[w] = 1
                break
        if prev == v:
            v = stack.pop()
    print(stack)

#-------------------------
import sys
sys.stdin = open('input.txt', 'r')

N = 10
for i in range(1, 1+N):
    V, E = map(int, input().split())
    a_list = list(map(int, input().split()))
    G = [[] for _ in range(V+1)]
    visit = [0 for _ in range(V+1)]
    for j in range(E):
        u, v = a_list[2*j], a_list[2*j+1]
        G[u].append(v)
DFS(2)



# def DFS(v):
#     for i in range(1, V+1):
#         if len(G[i]) == 0:



