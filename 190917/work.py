import sys; sys.stdin = open('input_work.txt', 'r')
def work(re, s):
    global result
    if s == rc:
        if result < re*100:
            result = re*100
        return
    elif re*100 < result:
        return
    else:
        for k in range(rc):
            if board[s][k] == 0:
                continue
            if visit[k] == False:
                visit[k] = True
                work(re*board[s][k], s+1)
                visit[k] = False




N = int(input())

for tc in range(1, N+1):
    rc = int(input())
    result = 0
    visit = [False for _ in range(rc)]
    board = [list(map(int, input().split())) for _ in range(rc)]
    for i in range(rc):
        for j in range(rc):
            board[i][j] /= 100
    work(1, 0)
    print('#{} {:.6f}'.format(tc, result))