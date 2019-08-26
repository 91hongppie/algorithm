import sys
sys.stdin = open('bomber5_input.txt', 'r')

N = int(input())
for i in range(1, N+1):
    row_col, num = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(row_col)]
    result = 0
    for j in range(num):
        row, col = map(int, input().split())
        result += sum(board[row])
        board[row] = [0] * row_col
        for k in range(row_col):
            result += board[k][col]
            board[k][col] = 0
    print('#{} {}'.format(i, result))

