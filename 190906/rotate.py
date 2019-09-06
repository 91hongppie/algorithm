import sys
sys.stdin = open('input_rotate.txt', 'r')

N = int(input())

for tc in range(1, N+1):
    rc = int(input())
    board = []
    for k in range(rc):
        board.append(list(map(str, input().split())))
    result = []
    for i in range(rc):
        a, b, d = '', '', ''
        for c in range(rc):
            a += board[-c-1][i]
            b += board[-i-1][-c-1]
            d += board[c][-i-1]
        result.append(a)
        result.append(b)
        result.append(d)
    print('#{}'.format(tc))
    for ya in range(1, len(result)+1):
        if ya % 3 == 0:
            print(result[ya-1])
        else:
            print(result[ya-1], end=' ')

    


