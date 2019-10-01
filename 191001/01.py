import sys
sys.stdin = open('01.txt', 'r')


def DFS(c):
    visit[c] = True
    for k in arr1[c]:
        if visit[k] == False:
            DFS(k)


N = int(input())

for tc in range(1, N+1):
    points, lines = map(int, input().split())
    visit = [False for _ in range(points+1)]
    arr1 = [[] for _ in range(points+1)]
    count = 0
    for _ in range(lines):
        arr = list(map(int, input().split()))
        arr1[arr[0]].append(arr[1])
        arr1[arr[1]].append(arr[0])
    for i in range(1, points+1):
        if visit[i] == False:
            DFS(i)
            count += 1
    print('#{} {}'.format(tc, count))
