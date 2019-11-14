import sys
sys.stdin = open('block.txt', 'r')

def DFS(row, col, block_map, nums):
    global result
    if nums == N:
        count = 0
        for g in range(H):
            for k in range(W):
                if block_map[g][k] != 0:
                    count += 1
        result = min(result, count)
        return
    crash(row, col, block_map)
    for h in range(H-1, -1, -1):
        for wi in range(W-1, -1, -1):
            if block_map[h][wi] == 0:
                for b in range(h, -1, -1):
                    if block_map[b][wi] != 0:
                        block_map[h][wi], block_map[b][wi] = block_map[b][wi], block_map[h][wi]
    for i in range(H):
        for j in range(W):
            if board[i][j] != 0 and (i == 0 or board[i-1][j] == 0):
                DFS(i, j, board, nums+1)


def crash(r, c, crash_map):
    if crash_map[r][c] == 1:
        crash_map[r][c] = 0
        return
    else:
        a = crash_map[r][c] - 1
        for u in range(r-a, r+a+1):
            if crash_map[u][c] > 1:
                crash(u, c, crash_map)
                crash_map[u][c] = 0 
            else:
                crash_map[u][c] = 0 
        for w in range(c-a, c+a+1):
            if crash_map[r][w] > 1:
                crash(r, w, crash_map)
                crash_map[r][w] = 0
            else:
                crash_map[r][w] = 0


N = int(input())

for tc in range(1, N+1):
    result = 1e9
    N, W, H = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(H)]
    for i in range(H):
        for j in range(W):
            if board[i][j] != 0 and (i == 0 or board[i-1][j] == 0):
                DFS(i, j, board, 1)