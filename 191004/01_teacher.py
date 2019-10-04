import sys
sys.stdin = open('01.txt', 'r')


def dfs(k, left, right, lsum, rsum):  # 0:초기값 1:왼쪽 2:오른쪽
    if lsum < rsum:
        return 0
    if k == N:
        return 1
    if dp[left][right] != -1:
        return dp[left][right]

    sum = 0
    for i in range(N):
        if used[i]:
            continue
        used[i] = True
        bit = 1 << i
        sum += dfs(k + 1, left + bit, right, lsum + data[i], rsum)
        sum += dfs(k + 1, left, right + bit, lsum, rsum + data[i])
        used[i] = False

    dp[left][right] = sum
    return sum


T = int(input())
for tc in range(T):
    N = int(input())
    data = list(map(int, input().split()))
    dp = [[-1 for _ in range(1 << 10)] for _ in range(1 << 10)]
    used = [False] * N

    ans = dfs(0, 0, 0, 0, 0)

    print("#%d %d" % (tc + 1, ans))
