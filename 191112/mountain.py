import sys
sys.stdin = open('mountain.txt', 'r')

def DFS(r, c, num, mount, k_value, k_num):
    global result
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    for j in range(4):
        x = r + dx[j]
        y = c + dy[j]
        if 0 <= x < rc and 0 <= y < rc:
            if visit[x][y] == False:
                if mount[x][y] < mount[r][c]:
                    visit[x][y] = True
                    DFS(x, y, num+1, mount, k_value, k_num)
                    visit[x][y] = False
                else:
                    if k_num == 1:
                        for yo in range(1, k_value+1):
                            if mount[x][y] - yo < mount[r][c]:
                                mount[x][y] = mount[x][y] - yo
                                visit[x][y] = True
                                DFS(x, y, num+1, mount, 0, 0)    
                                mount[x][y] = mount[x][y] + yo
                                visit[x][y] = False
    if result < num:
        result = num


N = int(input())
for tc in range(1, N+1):
    rc, k = map(int, input().split())
    mountain = []
    top = []
    result = 0
    max_value = 0
    visit = [[False]*rc for _ in range(rc)]
    for i in range(rc):
        mountain.append(list(map(int, input().split())))
        for y in range(rc):
            if mountain[i][y] > max_value:
                max_value = mountain[i][y]
    for p in range(rc):
        for n in range(rc):
            if mountain[p][n] == max_value:
                top.append([p, n])
    for l in range(len(top)-1, -1, -1):
        if visit[top[l][0]][top[l][1]] == False:
            visit[top[l][0]][top[l][1]] = True
            DFS(top[l][0], top[l][1], 1, mountain, k, 1)
            visit[top[l][0]][top[l][1]] = False
    print('#{} {}'.format(tc, result))