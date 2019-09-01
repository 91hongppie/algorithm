def distance(f, l, C):
    global count
    visit[f] = True
    a.append((f, C))
    if f == l:
        count= C
        return
    while a:
        h, s = a.pop(0)
        for i in G[h]:
            if i == l:
                count = s+1
                return
            elif not visit[i]:
                visit[i] = True
                a.append((i, s+1))

            



import sys
sys.stdin = open('sample_node.txt', 'r')
from queue import Queue

tc = int(input())
for i in range(1, tc+1):
    a = []
    node, line = map(int, input().split())
    G = [[] for _ in range(node+1)]
    visit = [False for _ in range(node+1)]
    for j in range(line):
        v, u = map(int, input().split())
        G[v].append(u)
        G[u].append(v)
    s, e = map(int, input().split())
    count = 0
    distance(s, e, 0)
    print('#{} {}'.format(i, count))

