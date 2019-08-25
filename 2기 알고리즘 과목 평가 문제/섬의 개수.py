def DFS(v, u):
    row = v
    col = u
    arr[row][col] = 0
    for k in range(row-1, row+2):
        for l in range(col-1, col+2):
            if arr[k][l] != 0:
                DFS(row, col)
    return

#---------------------------------------
import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
for i in range(N):
    rc = int(input())
    count = 0
    arr = [list(map(int, input().split())) for _ in range(rc)]
    for r in range(rc):
        for c in range(rc):
            if arr[r][c] != 0:
                DFS(r, c)
        count += 1
    print(count)




