import sys
sys.stdin = open('block.txt', 'r')
import copy
from pprint import pprint
from collections import deque

def DFS(r, c, block_map, nums):
    if nums == times:
        return
    if 0 <= r < H and 0 <= c < W:
        if block_map[r][c] == 1:
            for u in range(len(top_list)):
                if top_list[u] != -1:
                    block_map[top_list[u]][u] = 0
                    top_list[u] += 1
                    DFS(top_list[u], u, block_map, nums+1)
                    block_map[top_list[u]][u] = 1
                    top_list[u] -= 1

        else:
            Q.append([r, c])
            while Q:
                a, b = Q.popleft()
                for x in range(a-block_map[a][b]+1, a + block_map[a][b]):
                    if 0 <= x < H:
                        if block_map[x][b] != 0:
                            if block_map[x][b] == 1:
                                block_map[x][b] = 0
                            elif block_map[x][b] > 1:
                                Q.append([x, b])
                for y in range(b-block_map[a][b]+1, b + block_map[a][b]):
                    if 0 <= y < W:
                        if block_map[a][y] != 0:
                            if block_map[a][y] == 1:
                                block_map[a][y] = 0
                            elif block_map[a][y] > 1:
                                Q.append([a, y])
            for k in range(H-1 , -1, -1):
                for d in range(W-1, -1, -1):
                    if block_map[k][d] == 0:
                        for g in range(k, -1, -1):
                            if block_map[g][d] != 0:
                                block_map[k][d], block_map[g][d] = block_map[g][d], block_map[k][d]
            pprint(block_map)
            


N = int(input())

for tc in range(1, N+1):
    Q = deque()
    times, W, H = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(H)]
    a = copy.deepcopy(board)
    top_list = [-1 for _ in range(W)]
    print(top_list)
    for i in range(W):
        for j in range(H):
            if board[j][i]:
                top_list[i] = j
                break
    print(top_list)
    for k in range(W):
        if top_list[k] != -1:
            DFS(top_list[k], k, a, 0)

