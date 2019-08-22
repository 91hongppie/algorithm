# def DFS(v):
#     visit[v] = 1
#     for w in G[v]:
#         if not visit[w]:
#             DFS(w)

# # ----------------------------
# import sys
# sys.stdin = open('sample_input_01.txt', 'r')

# N = int(input())

# for i in range(1, N+1):
#     V, E = map(int, input().split())
#     G = [[] for _ in range(V+1)]
#     visit = [0 for _ in range(V+1)]
#     for j in range(E):
#         u, v = map(int, input().split())
#         G[u].append(v)

#     s, e = map(int, input().split())
#     DFS(s)
#     print(visit[e])

# 부분집합 --------------------------
arr = [1, 2, 3, 4]
n = len(arr)
result = []
for i in range(1<<n):
    a=[]
    for j in range(n):
        if i & (1<<j):
            a.append(arr[j])
    result.append(a)
print(result)