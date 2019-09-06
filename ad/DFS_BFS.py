import sys
sys.stdin  = open('DFS_BFS.txt', 'r')


def DFS(s):
    visit_DFS[s] = True
    stack.append(s)
    for ho in G[s]:
        if not visit_DFS[ho]:
            DFS(ho)

            
    
def BFS(s):
    visit_BFS[s] = True
    Q.append(s)
    stack_BFS.append(s)
    while Q:
        a = Q.pop(0)
        for yo in G[a]:
            if not visit_BFS[yo]:
                visit_BFS[yo] = True
                Q.append(yo)
                stack_BFS.append(yo)


        

point, line, start_point = map(int, input().split())
visit_DFS = [False for _ in range(point+1)]
visit_BFS = [False for _ in range(point+1)]
G = [[] for _ in range(point+1)]
Q = []
stack = []
stack_BFS = []
for i in range(line):
    v, e = map(int, input().split())
    G[v].append(e)
    G[e].append(v)
for u in range(len(G)):
    G[u] = sorted(G[u])
DFS(start_point)

print(*stack)
BFS(start_point)

print(*stack_BFS)
