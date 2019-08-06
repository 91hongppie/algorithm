import sys
sys.stdin  = open("sample_input_01.txt", "r")


N = int(input())
board = [[0]*10 for _ in range(10)]

for i in range(1, N+1):
    count = int(input())
    board = [[0] * 10 for _ in range(10)]
    counts = 0
    for c in range(count):
        result = list(map(int, input().split()))
        for x in range(result[0], result[2]+1):
            for y in range(result[1], result[3]+1):
                if board[x][y] == 0:
                    board[x][y] = result[-1]
                elif board[x][y] != 0 and result[-1] != board[x][y]:
                        counts += 1
    print('#{} {}'.format(i, counts))






