import sys
sys.stdin = open('bomber1_input.txt', 'r')

N = int(input())

for i in range(1, N+1):
    num = int(input())
    board = [list(map(int, input().split())) for _ in range(num)]
    result = 0
    for r in range(num):
        row_sum = col_sum = 0
        for c in range(num):
            row_sum = sum(board[r])
            col_sum += (board[r][c])
        if result < row_sum + col_sum:
            result = row_sum + col_sum
            R = r
            C = c
    print(R, C, result)
