import sys
sys.stdin = open('01.txt', 'r')


def cal(num, cnt):
    global count
    if num > 1000000:
        return
    if cnt > count:
        return
    if dp[num] != -1:
        if dp[num] > cnt:
            dp[num] = cnt
        else:
            return
    else:
        dp[num] = cnt
    if num == e_num:
        if count <= cnt:
            return
        count = cnt
        return
    if 0 <= num < e_num:
        cal(num*2, cnt+1)
        cal(num+1, cnt+1)
    cal(num-1, cnt+1)
    cal(num-10, cnt+1)


N = int(input())
for tc in range(1, N+1):
    s_num, e_num = map(int, input().split())
    count = 1000000
    dp = [-1] * 1000000
    cal(s_num, 0)
    print('#{} {}'.format(tc, count))
