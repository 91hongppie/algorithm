
import sys
sys.stdin = open('03.txt', 'r')


def kruskal(num, cnt):
    global result
    if cnt == points:
        return
    # if k[G[num][1]][1] == k[G[num][2]][1]:
    #     kruskal(num+1, cnt)
    k[G[num][2]][1] = G[num][1]
    result[G[num][1]] += G[num][0]
    kruskal(num+1, cnt+1)


N = int(input())

for tc in range(1, N+1):
    points, lines = map(int, input().split())
    G = []
    for k in range(lines):
        a = list(map(int, input().split()))
        G.append([a[2], a[0], a[1]])
    k = []
    for y in range(points+1):
        k.append([y, y])
    G.sort()
    result = [0 for _ in range(points+1)]
    print(G)
    kruskal(0, 0)
    print(k)
    print('#{} {}'.format(tc, sum(result)))
