import sys
sys.stdin = open('bishop.txt', 'r')
sys.setrecursionlimit(10**8)

def bishop(yo, cnt):
    global po, result
    if yo == len(po):
        result = max(result, cnt)
    else:
        r, c = po[yo][0], po[yo][1]
        i = r + 1
        j = c + 1
        v = 0
        while 0 <= i and i < N and 0 <= j and j < N:
            if board[i][j] == 2:
                v += 1
                break
            i += 1
            j += 1
        if v == 0:
            i = r - 1
            j = c - 1
            while 0 <= i and i < N and 0 <= j and j < N:
                if board[i][j] == 2:
                    v += 1
                    break
                i -= 1
                j -= 1
        if v == 0:
            i = r + 1
            j = c - 1
            while 0 <= i and i < N and 0 <= j and j < N:
                if board[i][j] == 2:
                    v += 1
                    break
                i += 1
                j -= 1
        if v == 0: 
            i = r - 1 
            j = c + 1
            while 0 <= i and i < N and 0 <= j and j < N:
                if board[i][j] == 2:
                    v += 1
                    break
                i -= 1
                j += 1
        if v == 0:
            board[r][c] = 2
            bishop(yo+1, cnt+1)
            board[r][c] = 1
            bishop(yo+1, cnt)
        else:
            bishop(yo+1, cnt)






N = int(input())
board = []
po = []
result = 0
for _ in range(N):
    board.append(list(map(int, input().split())))
for i in range(N):
    for j in range(N):
        if board[i][j] == 1:
            po.append([i, j, 0])

bishop(0, 0)
print(result)