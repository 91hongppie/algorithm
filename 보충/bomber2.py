import sys
sys.stdin = open('bomber2.txt', 'r')


N = int(input())

for i in range(1, N+1):
    result = 0
    num = int(input())
    board = [list(map(int, input().split())) for _ in range(num)]
    for j in range(num):
        for k in range(num):
            r = a = j
            c = b = k
            result_sum = 0
            while r != 0 and c != 0:
                r -= 1
                c -= 1
            while r < num and c < num:
                result_sum += board[r][c]
                r += 1
                c += 1
            reverse_sum = 0
            while a != 0 and b < num-1:
                a -= 1
                b += 1
            while a < num and b >= 0:
                reverse_sum += board[a][b]
                a += 1
                b -= 1
            bomb = result_sum + reverse_sum - board[j][k]
            if result <= bomb:
                result = bomb
                row = j
                col = k
    print('#{} {} {} {}'.format(i, row, col, result))

                




                
                    

                

