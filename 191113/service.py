import sys
sys.stdin = open('service.txt', 'r')

def cost(r, c):
    global result
    for u in range(1, rc+2):
        rang = 0
        count = 0
        for k in range(r-(u-1), r+(u-1)+1):
            if 0 <= k < rc:
                for y in range(c-rang, c+rang+1):
                    if 0 <= y < rc:
                        if board[k][y] == 1:
                            count += 1
            if k < r:
                rang += 1
            else:
                rang -= 1
        run_cost = u ** 2 + (u-1) ** 2
        income = count * M
        if income-run_cost >= 0:
            if count > result:
                result = count


N = int(input())
for tc in range(1, N+1):
    rc, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(rc)]
    result = 0
    for i in range(rc):
        for j in range(rc):
            cost(i, j)
    print('#{} {}'.format(tc, result))