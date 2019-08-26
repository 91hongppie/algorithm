import sys
sys.stdin = open('input_sum.txt', 'r')

for i in range(1, 11):
    tc = int(input())
    board = [list(map(int, input().split())) for _ in range(100)]
    result = 0
    back_slash = 0
    slash = 0
    for j in range(100):
        row = sum(board[j])
        back_slash += board[j][j]
        slash += board[j][-1-j]
        c = 0
        col = 0
        while c < 100:
            col += board[c][j]
            c += 1
        result = max(col, row, result)
    result = max(result, back_slash, slash)
    print('#{} {}'.format(i, result))
            
