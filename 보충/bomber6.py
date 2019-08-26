import sys
sys.stdin = open('bomber6_input.txt', 'r')

N = int(input())
for i in range(1, N+1):
    row_col, num = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(row_col)]
    result = 0
    for j in range(num):
        row, col, bomb_range = map(int, input().split())
        for r in range(col-bomb_range, col+bomb_range+1):
            if r < 0 or r >= row_col:
                pass
            else:
                result += board[row][r]
                board[row][r] = 0
        for c in range(row-bomb_range, row+bomb_range+1):
            if c < 0 or c >= row_col:
                pass
            else:
                result += board[c][col]
                board[c][col] = 0
    print('#{} {}'.format(i, result))
                    
