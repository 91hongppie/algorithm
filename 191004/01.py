import sys
sys.stdin = open('01.txt', 'r')


def comb(e, n):
    global com
    if n == nums:
        a = com[::]
        result.append(a)
        return
    for k in range(1, nums+1):
        if not visit[k]:
            com.append(num_list[k-1])
            visit[k] = True
            comb(e+1, n+1)
            com.pop()
            visit[k] = False


def calc(num, s):
    global left_we, right_we, count
    if s == nums:
        count += 1
        return
    else:
        if left_we >= right_we + result[num][s]:
            left_we += result[num][s]
            calc(num, s+1)
            left_we -= result[num][s]
            right_we += result[num][s]
            calc(num, s+1)
            right_we -= result[num][s]
        else:
            left_we += result[num][s]
            calc(num, s+1)
            left_we -= result[num][s]


N = int(input())
for tc in range(1, N+1):
    nums = int(input())
    com = []
    result = []
    num_list = list(map(int, input().split()))
    visit = [False for _ in range(nums+1)]
    comb(1, 0)
    count = 0
    dp = [[-1 for _ in range(1 << 10)] for _ in range(1 << 10)]
    for u in range(len(result)):
        left_we = 0
        left_we += result[u][0]
        right_we = 0
        calc(u, 1)
    print('#{} {}'.format(tc, count))
