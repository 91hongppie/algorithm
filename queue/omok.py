import sys
sys.stdin = open('input_omok.txt', 'r')
board = []
x = y = 0
for _ in range(19):
    board.append(list(map(int, input().split())))
for i in range(len(board)):
    for j in range(len(board[i])):
        if board[i][j] == 1:
            x, y = i, j
            num = board[i][j]
            # print(x, y)
            for k in range(2):
                for l in range(-1, 2):
                    if board[i+k][j+l] == 1:
                        mx, my = k, l
        elif board[i][j] == 2:
            x, y = i, j
            num = board[i][j]
            for k in range(2):
                for l in range(-1, 2):
                    if board[i+k][j+l] == 2:
                        mx, my = k, l
        lx, ly = x, y
        count = 0
        if board[lx][ly] != 0:
            while board[lx][ly] == num:
                lx += mx
                ly += my
                count += 1
        if count == 5:
            print(num)
            print(x, y)
            exit()





