import sys
sys.stdin = open('input_quiz.txt', 'r')

N = int(input())

for tc in range(1, N+1):
    rc, word_length = map(int, input().split())
    board = []
    for j in range(rc):
        board.append(list(map(int, input().split())))
    board2 = [[] for _ in range(rc)]
    for r in range(len(board)):
        for c in range(len(board)):
            board2[r].append(board[c][r])
    i = 0
    result = 0
    while i < len(board):
        count = 0
        count2 = 0
        for h in range(len(board)):
            if board[i][h] == 0:
                count = 0
            else:
                count += 1
                if count == word_length:
                    if h == len(board)-1 or board[i][h+1] == 0:
                        result += 1
            if board2[i][h] == 0:
                count2 = 0
            else:
                count2 += 1
                if count2 == word_length:
                    if h == len(board)-1 or board2[i][h+1] == 0:
                        result += 1

        i += 1
    print('#{} {}'.format(tc, result))
