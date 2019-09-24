import sys
sys.stdin = open('sample_nqueen.txt', 'r')


def chess(s, e, arr):
    for y in range(rc)
       if 1 not in board[s]:
            for u in range(rc):
                if board[u][e] == 1:
                    break
        else:
            board[s][e] = 1


N = int(input())

for tc in range(1, N+1):
    rc = int(input())
    board = []
    for i in range(rc):
        board.append([0 for _ in range(rc)])
    if rc == 1:
        print('#{} 1'.format(tc))
    else:
        for k in range(rc):
            chess(0, k, board)
