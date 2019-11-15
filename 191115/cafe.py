import sys
sys.stdin = open('cafe.txt', 'r')
from pprint import pprint

def DFS(r, c, k, nums, ca_list):
    global result
    if r == a+1  and c == b-1 and len(ca_list) > 2 :
        result = max(result, len(ca_list))
        return
    if r == a and c == b and nums == 0:
        x = r + 1
        y = c + 1
        if board[x][y] not in ca_list:
            ca_list.append(board[x][y])
            DFS(x, y, 3, nums+1, ca_list)
            ca_list.pop()
        else:
            return
    for u in k_list[k]:
        x = r + dx[u]
        y = c + dy[u]
        if 0 <= x < rc and 0 <= y < rc:
            if board[x][y] not in ca_list:
                if nums == 0 and u ==0:
                    continue
                if u == 3:
                    nums += 1
                elif u == 0:
                    nums -= 1
                ca_list.append(board[x][y])
                DFS(x, y, u, nums, ca_list)
                ca_list.pop()
 
    

k_list = [[0, 1], [1], [2, 0], [3, 2]]
dx = [-1, -1, 1, 1]
dy = [-1, 1, -1, 1] # 0:좌상, 1:우상, 2:좌하, 3:우하
N = int(input())

for tc in range(1, N+1):
    rc = int(input())
    board = [list(map(int, input().split())) for _ in range(rc)]
    visit = [[False]*rc for _ in range(rc)]
    result = 0
    cafe_list = []
    for i in range(rc-2):
        for j in range(1, rc-1):
                cafe_list.append(board[i][j])
                dir_list = [0, 0, 0, 0]
                a, b = i, j
                DFS(i, j, 3, 0, cafe_list)
                cafe_list.pop()
    if result == 0:
        result = -1
    print('#{} {}'.format(tc, result))
