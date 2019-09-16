import sys; sys.stdin = open('input_kart.txt', 'r')

def kart(re, s, e):
    global result
    if e == rc:
        result = min(result, re)
        return
    if re > result:
        return
    for i in range(rc):
        if i == 0:
            if e != rc-1:
                continue
            elif e == rc-1:
                kart(re+board[s][i], i, e+1)
        elif board[s][i] == 0:
            continue
        elif visit[i] == False:
            visit[i] = True
            kart(re+board[s][i], i, e+1)
            visit[i] = False

N =int(input())

for tc in range(1, N+1):
    rc = int(input())
    visit = [False for _ in range(rc)]
    board = [list(map(int, input().split())) for _ in range(rc)]
    result = 1e9
    kart(0, 0, 0)
    print('#{} {}'.format(tc, result))