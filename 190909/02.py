import sys
sys.stdin = open('02.txt', 'r')

N = int(input())

for i in range(1, N+1):
    row, length = map(int, input().split())
    password = ['0001101', '0011001', '0010011', '0111101', '0100011', '0110001', '0101111', '0111011', '0110111', '0001011']

    board = [list(map(str, input())) for _ in range(row)]
    a = b = 0
    for j in range(row):
        for k in range(length):
            if board[j][k] == '1':
                a, b = j, k
        if a != 0 and b != 0:
            break
    b -= 55
    result = []
    for y in range(b, b+55, 7):
        c = ''
        for u in range(y, y+7):
            c += board[a][u]
        result.append(c)
    result_num = []
    for h in result:
        result_num.append(password.index(h))
    first = last = kkk = 0 
    for yo in range(0, len(result_num), 2):
        first += result_num[yo]
        last += result_num[yo+1]
    kkk = first + last
    first = first * 3
    first += last
    if not first % 10:
        print('#{} {}'.format(i, kkk))
    else:
        print('#{} 0'.format(i))

        

