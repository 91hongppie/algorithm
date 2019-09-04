def DFS(r, c, dx, dy, color):
    global board
    if 0 <= r+dx < len(board) and 0 <= c+dy < len(board):
        if board[r+dx][c+dy] != color and board[r+dx][c+dy] != 0:
            p = DFS(r+dx, c+dy, dx, dy, color)
            if p == '2':
                board[r+dx][c+dy] = color
                return '2'
        elif board[r+dx][c+dy] == color and board[r+dx][c+dy] != 0:
            return '2'

        

import sys
sys.stdin = open('sample_game.txt', 'r')

N = int(input())

for z in range(1, N+1):
    rc, nums = map(int, input().split())
    board = [[0]* rc for _ in range(rc)]
    board[len(board)//2-1][len(board)//2-1] = 2
    board[len(board)//2-1][len(board)//2] = 1
    board[len(board)//2][len(board)//2] = 2
    board[len(board)//2][len(board)//2-1] = 1
    
    for j in range(nums):
        r, c, color = map(int, input().split())
        board[r-1][c-1] = color
        dx = [1, -1, 0, 0, 1, 1, -1, -1]
        dy = [0, 0, 1, -1, -1, 1, 1, -1]
        i = 0
        while i < 8:
            x = r - 1  + dx[i]
            y = c - 1 + dy[i]
            i+=1
            if 0 <= x < len(board) and 0 <= y < len(board) and color == 2 and board[x][y] == 1:
                DFS(r-1, c-1, x-(r-1), y-(c-1), color)
            elif 0 <= x < len(board) and 0 <= y < len(board) and color == 1 and board[x][y] == 2:
                DFS(r-1, c-1, x-(r-1), y-(c-1), color)
        one = 0
        two = 0
        for x in board:
            one += x.count(1)
            two += x.count(2)
    print('#{} {} {}'.format(z, one, two))
    