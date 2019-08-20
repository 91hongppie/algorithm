import sys
sys.stdin = open('bomber3_input.txt', 'r')

N = int(input())

for u in range(1, N+1):
    num, bomb = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(num)]
    bomb_sum = 0
    for i in range(num - bomb + 1):
        for j in range(num - bomb +1):
            result = 0
            for row in range(i, i + bomb):
                for col in range(j, j + bomb):
                    result += board[row][col]
                if result > bomb_sum:
                    bomb_sum = result
                    I = i
                    J = j
    print('#{} {} {} {}'.format(u, I, J, bomb_sum))

