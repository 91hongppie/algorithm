from itertools import combinations
import sys
sys.stdin = open('bee.txt', 'r')


def bee(r, c, box, df, cnt):
    global result
    if c == j + (workers):
        result.append([df, i, j, c])
        return
    if cnt == 5:
        return
    if 0 <= r < rc and 0 <= c < rc:
        if box - board[r][c] >= 0:
            bee(r, c+1, box-board[r][c], df+(board[r][c])**2, cnt+1)
            bee(r, c+1, box, df, cnt)
        else:
            bee(r, c+1, box, df, cnt)
            return
    # if c == rc:
    #     result.append([df, i, j, j+workers-1])


def comb(num, arr, cnt):
    global result_honey
    yo = 0
    for y in arr:
        yo += y[0]
    if result_honey > yo:
        return
    if num == len(result)-1:
        return
    if cnt == 2:
        honey = 0
        for k in arr:
            honey += k[0]
        result_honey = max(result_honey, honey)
        return
    ho = 0
    for k in arr:
        if k[1] == result[num+1][1]:
            if k[2] <= result[num+1][2] <= k[3] or k[2] <= result[num+1][3] <= k[3]:
                ho += 1
    if ho == 0:
        arr.append(result[num+1])
        comb(num+1, arr, cnt+1)
        arr.pop()
        comb(num+1, arr, cnt)
    else:
        comb(num+1, arr, cnt)


N = int(input())

for tc in range(1, N+1):
    rc, workers, vol = map(int, input().split())
    board = []
    result = []
    result_honey = 0
    for _ in range(rc):
        board.append(list(map(int, input().split())))
    for i in range(rc):
        for j in range(rc-(workers-1)):
            bee(i, j, vol, 0, 0)
    result.sort(reverse=True)
    # print(result)
    for u in range(len(result)):
        c = []
        c.append(result[u])
        comb(u, c, 1)
    print('#{} {}'.format(tc, result_honey))
