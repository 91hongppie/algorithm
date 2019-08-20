import sys
sys.stdin = open('input_ladder.txt', 'r')
board = [[] for _ in range(100)]

for num in range(10):
    num = int(input())
    for j in range(100):
        board[j] = list(map(int, input().split()))
    first = board[99].index(2)
    i, j = 98, first
    while i >= 0:
        if j < 99 and board[i][j+1] == 1:
            while j < 99 and board[i][j+1] == 1:
                j += 1
            i -= 1
        elif board[i][j-1] == 1:
            while board[i][j-1] == 1 and j > 0:
                j -= 1
            i -= 1
        elif board[i][j] == 1 and board[i-1][j] == 1:
            i -= 1
    
    print('#{} {}'.format(num, j))


            


