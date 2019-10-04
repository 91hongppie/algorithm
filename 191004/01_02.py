import sys
sys.stdin = open('01.txt', 'r')


def dfs(e, l, r, left, right):
    if right > left:
        return 0
    if e == nums:
        return 1
    if dp[l][r] != -1:
        return dp[l][r]
    count = 0
    for i in range(nums):
        if not visit[i]:
            visit[i] = True
            count += dfs(e+1, l+2**i, r, left+num_list[i], right)
            count += dfs(e+1, l, r+2**i, left, right+num_list[i])
            visit[i] = False
    dp[l][r] = count
    return count


N = int(input())
for tc in range(1, N+1):
    nums = int(input())
    com = []
    result = []
    num_list = list(map(int, input().split()))
    visit = [False for _ in range(nums)]
    count = 0
    dp = [[-1 for _ in range(1 << 10)] for _ in range(1 << 10)]
    print('#{} {}'.format(tc, dfs(0, 0, 0, 0, 0)))
