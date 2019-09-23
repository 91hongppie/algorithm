import sys
sys.stdin = open('crazy.txt', 'r')


def DFS(r, c, per, cnt):
    global percent, visit
    if cnt == num:
        percent += per
        return
    for k in range(4):
        if result[k][0] == 'E':
            x = r
            y = c + 1
            if visit[x][y] == False:
                visit[x][y] = True
                DFS(x, y, per*result[k][1], cnt+1)
                visit[x][y] = False
        elif result[k][0] == 'W':
            x = r
            y = c - 1
            if visit[x][y] == False:
                visit[x][y] = True
                DFS(x, y, per*result[k][1], cnt+1)
                visit[x][y] = False
        elif result[k][0] == 'S':
            x = r + 1
            y = c
            if visit[x][y] == False:
                visit[x][y] = True
                DFS(x, y, per*result[k][1], cnt+1)
                visit[x][y] = False
        elif result[k][0] == 'N':
            x = r - 1
            y = c
            if visit[x][y] == False:
                visit[x][y] = True
                DFS(x, y, per*result[k][1], cnt+1)
                visit[x][y] = False


num, E, W, S, N = map(int, input().split())
result = [['E', E/100], ['W', W/100], ['S', S/100], ['N', N/100]]
visit = [[False]*29 for _ in range(29)]

visit[14][14] = True
percent = 0
DFS(14, 14, 1, 0)
print(percent)
