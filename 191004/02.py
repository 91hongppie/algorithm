import sys
sys.stdin = open('02.txt', 'r')


def dfs(num, cnt):
    if time_table[num] == 0:
        dfs(num+1, cnt)
    else:


N = int(input())
for tc in range(1, N+1):
    daily, month, th_months, year = map(int, input().split())
    time_table = list(map(int, input().split()))
    dfs(0, 0)
