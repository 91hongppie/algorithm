import sys
sys.stdin = open('04 Stack1_DFS_input.txt', 'r')

V, E = map(int, input().split()) # 정점수, 간선수

G = [[] for _ in range(V + 1)] #  정점 번호 1 ~ V

for _ in range(E):
    u, v = map(int, input().split())
    G[u].append(v)
    G[v].append(u)

for i in range(1, V+1):
    print(i, '-->', G[i])


import sys
sys.stdin = open('04 Stack1_DFS_input.txt', 'r')

def DFS(v): # v: 시작점
    S = []
    visit = [False] * (V + 1)
    
    visit[v] = True # 시작점을 방문한다.
    S.append(v) # 시작점을 스택에 push

    while S:  # 빈스택이 아닐 동안
        # v의 방문하지 않은 인접정점을 찾는다. ==> w
        for w in G[v]:
            if not visit[w]:
                visit[w] = True # w를 방문하고
                print(w, end=' ')
                S.append(v) # v를 스택에 push
                v = w   # w를 현재 방문하는 정점으로 설정
                break
        else:           # 이전에 방문한 정점으로 되돌아 간다.
            v = S.pop()

V, E = map(int, input().split()) # 정점수, 간선수
G = [[] for _ in range(V + 1)] #  정점 번호 1 ~ V

for _ in range(E):
    u, v = map(int, input().split())
    G[u].append(v)
    G[v].append(u)


DFS(1)

def DFS(v):
    visit[v] = True; print(v, end=' ')
    for w in G[v]:
        if not visit[w]:
            DFS(w)