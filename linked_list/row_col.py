import sys
sys.stdin = open('input_row_col.txt', 'r')

N = int(input())

for i in range(1, N+1):
    rc = int(input())
    table = []
    for j in range(rc):
        table.append(list(map(int, input().split())))
    i = 0
    j = 0
    while i < len(table):
        while j < len(table):
            r = c = 1
            a, b = i, j
            while table[i][j] != 0:
                while table[i][j] != 0:
                    table[i][j] = 0
                    if table[i][j+1] != 0:
                        j += 1
                        c += 1
                    elif table[i][j+1] == 0 and table[i+1][j] != 0:
                        j = b
                        i += 1
                        r += 1
                    elif table[i+1][j] == 0 and table[i][j+1] == 0:
                        break
            i = a
            j = b
            print(r, c)
            j += b
        i += 1
                
    print(i) 
            

