from pprint import pprint
import sys
sys.stdin = open('block.txt', 'r')
import copy
from collections import deque
from itertools import product
def DFS(cols, go_list, nums):
    global result
    b = copy.deepcopy(go_list)
    for col in cols:
        for k in range(H):
            if b[k][col] != 0:
                if b[k][col] == 1:
                    b[k][col] = 0
                else:
                    b = BFS(k, col, b)
                    b = clean(b)
                break
    io = 0
    for k in range(H):
        io += b[k].count(0)
    c = W*H - io
    if c < result:
        result = c
    return


def BFS(r, c, b_list):
    A = set()
    visit = [[0]*W for _ in range(H)]
    Q.append([r, c])
    while Q:
        a, b = Q.popleft()
        for w in range(a-b_list[a][b]+1, a+b_list[a][b]):
            if 0 <= w < H:
                if visit[w][b] == 0:
                    A.add((w, b))
                    visit[w][b] = 1
                    if b_list[w][b] == 1 or b_list[w][b] == 0:
                        continue
                    Q.append([w, b])
        for u in range(b-b_list[a][b]+1, b+b_list[a][b]):
            if 0 <= u < W:
                if visit[a][u] == 0:
                    A.add((a, u))
                    visit[a][u] = 1
                    if b_list[a][u] == 1 or b_list[a][u] == 0:
                        continue
                    Q.append([a, u])
    for y, u in A:
        b_list[y][u] = 0
    return b_list

def clean(b_list):
    for co in range(W-1, -1, -1):
        for ro in range(H-1, -1, -1):
            if b_list[ro][co] == 0:
                for uy in range(ro, -1, -1):
                    if b_list[uy][co] != 0:
                        b_list[ro][co], b_list[uy][co] = b_list[uy][co], b_list[ro][co]
                        break
    return b_list
            


N = int(input())

for tc in range(1, N+1):
    Q = deque()
    result = 1e9
    times, W, H = map(int, input().split())
    a = product([i for i in range(W)], repeat=times)
    a = list(a)
    # print(a)
    board = [list(map(int, input().split())) for _ in range(H)]
    for i in a:
        DFS(i, board, 0)
        if result == 0:
            break
    print('#{} {}'.format(tc, result))
    