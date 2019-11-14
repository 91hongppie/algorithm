import sys
sys.stdin = open('cafe.txt', 'r')
from pprint import pprint

def DFS(r, c, nums, ca_list):
    global result
    if abs(r-i) == 1 and abs(c-j) == 1:
        if nums > 2:
            result = max(result, nums)
            print(ca_list)
            pprint(visit)
            return
    for k in range(4):
        x = r + dx[k]
        y = c + dy[k]
        if 0 <= x < rc and 0 <= y < rc:
            if board[x][y] in ca_list:
                continue
            if visit[x][y] == False:
                visit[x][y] = True
                ca_list.append(board[x][y])
                DFS(x, y, nums+1, ca_list)
                ca_list.pop()
                visit[x][y] = False


dx = [-1, 1, -1, 1]
dy = [-1, 1, 1, -1]
N = int(input())

for tc in range(1, N+1):
    rc = int(input())
    board = [list(map(int, input().split())) for _ in range(rc)]
    visit = [[False]*rc for _ in range(rc)]
    result = 0
    cafe_list = []
    for i in range(rc):
        for j in range(i, rc):
            if i == 0:
                if j == 0 or j == rc-1:
                    continue
            elif i == rc-1 and j == rc-1:
                continue
            if visit[i][j] == False:
                visit[i][j] = True
                cafe_list.append(board[i][j])
                DFS(i, j, 1, cafe_list)
                cafe_list.pop()
                visit[i][j] = False
    print(result)
