import sys
sys.stdin = open('bomber1_input.txt', 'r')

N = int(input())

for i in range(1, N+1):
    num = int(input())
    board = [list(map(int, input().split())) for _ in range(num)]
    result = 0

    for r in range(num):
        row_sum = 0
        row_sum = sum(board[r])
        for s in range(num):
            col_sum = 0
            for c in range(num):
                if c == r:
                    pass
                else:    
                    col_sum += (board[c][s])
            if result <= row_sum + col_sum:
                result = row_sum + col_sum
                R = r
                C = s
    print('#{} {} {} {}'.format(i, R, C, result))
