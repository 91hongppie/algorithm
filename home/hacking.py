import sys
sys.stdin = open('hacking.txt', 'r')

nodes, lines = map(int, input().split())
G = [[] for _ in range(nodes+1)]
visit = [False for _ in range(nodes+1)]
for _ in range(lines):
    u, e = map(int, input().split())
    G[u].append(e)
    G[e].append(u)
