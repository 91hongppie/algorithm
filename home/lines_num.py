import sys
sys.stdin = open('lines_num.txt', 'r')


def DFS(num):
    for k in G[num]:
        if visit[k] == False:
            visit[k] = True
            DFS(k)


points, lines = map(int, input().split())
G = [[] for _ in range(points+1)]
visit = [False for _ in range(points+1)]
result = 0
for _ in range(lines):
    u, e = map(int, input().split())
    G[u].append(e)
    G[e].append(u)
for i in range(1, len(G)):
    if visit[i] == False:
        visit[i] = True
        DFS(i)
        result += 1
print(result)
