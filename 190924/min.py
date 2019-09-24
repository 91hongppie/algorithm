import sys
sys.stdin = open('sample_min.txt', 'r')


def work(e, sums, c):
    global result
    if sums >= result:
        return
    if c == rc:
        result = min(result, sums)
        return
    for j in range(rc):
        if not visit[j]:
            visit[j] = True
            work(j, sums+work_list[c][j], c+1)
            visit[j] = False


N = int(input())
for tc in range(1, N+1):
    rc = int(input())
    work_list = []
    result = 1e9
    visit = [False for _ in range(rc)]
    for _ in range(rc):
        work_list.append(list(map(int, input().split())))
    for i in range(rc):
        visit[i] = True
        work(i, work_list[0][i], 1)
        visit[i] = False
    print('#{} {}'.format(tc, result))
