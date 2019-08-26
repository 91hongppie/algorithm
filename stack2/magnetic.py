import sys; sys.stdin = open('input_magnetic.txt', 'r')

for i in range(1, 11):
    N = int(input())
    table =[list(map(int, input().split())) for _ in range(N)]
    result = 0
    for j in range(N):
        k = 0
        count = 0
        while k < N:
            if table[k][j] == 1:
                count += 1
            elif table[k][j] == 2 and count > 0:
                result += 1
                count = 0
            k+=1              
    print('#{} {}'.format(i, result))

