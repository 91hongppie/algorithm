import sys
sys.stdin = open('bomber4_input.txt', 'r')

N = int(input())

for i in range(1, N+1):
    V, E = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(V)]
    result = 0
    for j in range(E):
        row, col, bomb_range = map(int, input().split())
        for r in range(row, row+bomb_range):
            for c in range(col, col+bomb_range):
                if c < V and r < V:
                    result += board[r][c]
                    board[r][c] = 0
                else:
                    pass
    print('#{} {}'.format(i, result))
    