from collections import deque
import sys
sys.stdin = open('01.txt', 'r')


def cal(num, cnt):
    Q.append([num, cnt])
    while Q:
        a, b = Q.popleft()
        if dp[a] != -1:
            if dp[a] <= b:
                continue
            else:
                dp[a] = b
        else:
            dp[a] = b
        if a == s_num:
            print('#{} {}'.format(tc, b))
            break
        if a % 2 == 0:
            Q.append([a//2, b+1])
        if 0 < a - 1:
            Q.append([a-1, b+1])
        if a + 1 < 1000000:
            Q.append([a+1, b+1])
        if a + 10 < 1000000:
            Q.append([a+10, b+1])


N = int(input())
for tc in range(1, N+1):
    s_num, e_num = map(int, input().split())
    dp = [-1 for _ in range(1000001)]
    Q = deque()
    cal(e_num, 0)
