from queue import Queue
import sys
sys.stdin = open('03.txt', 'r')

def Q(u):
    q.put(u)
    while q:
        a = q.get()
        if not visit[a]:
            print(a, end='')
            visit[a] = True
            for i in G[a]:
                if not visit[i]:
                    q.put(i)

        

q = Queue()
V, E = 7, 8
visit = [False for _ in range(V+1)]
G = [[] for _ in range(V+1)]

for i in range(E):
    v, u = map(int, input().split())
    G[v].append(u)
    G[u].append(v)
Q(1)


    
