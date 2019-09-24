import sys
sys.stdin = open('sdoku.txt', 'r')
sys.setrecursionlimit(10**9)

def sdoku(r, c, board):
    if board[r][c] != 0:
        if c == 8 and r == 8:
            for k in board:
                print(*k)
            exit()
        if c == 8:
            sdoku(r+1, 0, board)
            return
        else:
            sdoku(r, c+1, board)
            return
            
    nums = []
    for l in range(9):
        cnt = 0
        if l+1 not in board[r]:
            for m in range(9):
                if board[m][c] == l+1:
                    cnt = 1
                    break
            x = r // 3 * 3
            y = c // 3 * 3
            for x1 in range(x, x+3):
                for y1 in range(y, y+3):
                    if board[x1][y1] == l+1:
                        cnt = 1
                        break
            if cnt == 0: 
                nums.append(l+1)
            
    
    if len(nums) == 0:
        return
    for k in nums:
        if r == 8 and c == 8:
            board[r][c] = k
            for k in board:
                print(*k)
            exit()
        elif c == 8:
            board[r][c] = k
            sdoku(r+1, 0, board)
            board[r][c] = 0           
        else:
            board[r][c] = k
            sdoku(r, c+1, board)
            board[r][c] = 0

    return


board = []
for i in range(9):
    board.append(list(map(int, input().split())))
sdoku(0, 0, board)
