import sys
sys.stdin = open('deli.txt', 'r')


def deli(cnt, r, c, dis):
    global result
    if dis >= result:
        return
    if cnt == len(arr):
        dis += abs(r-home[0])+abs(c-home[1])
        result = min(result, dis)
        return
    for i in range(nums):
        if visit[i] == False:
            visit[i] = True
            x = arr[i][0]
            y = arr[i][1]
            deli(cnt+1, x, y, dis +
                 (abs(x-r)+abs(y-c)))
            visit[i] = False


N = int(input())
for tc in range(1, N+1):
    nums = int(input())
    leng = list(map(int, input().split()))
    com = leng[0:2]
    home = leng[2:4]
    leng = leng[4::]
    result = 1e9
    arr = []
    for k in range(0, len(leng), 2):
        arr.append([leng[k], leng[k+1]])
    visit = [0]*nums
    deli(0, com[0], com[1], 0)
    print('#{} {}'.format(tc, result))
