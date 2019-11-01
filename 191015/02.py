import sys
sys.stdin = open('02.txt', 'r')


def DFS(num):
    for u in G[num]:
        if not visit[u]:
            visit[u] = True
            DFS(u)


N = int(input())

for tc in range(1, N+1):
    nums, lines = map(int, input().split())
    line_list = list(map(int, input().split()))
    G = [[] for _ in range(nums+1)]
    visit = [False for _ in range(nums+1)]
    for k in range(0, len(line_list), 2):
        G[line_list[k]].append(line_list[k+1])
        G[line_list[k+1]].append(line_list[k])
    cnt = 0
    for u in range(1, nums+1):
        if not visit[u]:
            visit[u] = True
            DFS(u)
            cnt += 1
    print('#{} {}'.format(tc, cnt))
