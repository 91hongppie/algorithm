def DFS(r, c):
    tb = [-1, +1]
    maze[r][c] = 1
    global result
    for h in tb:
        if r+h >= 0 and r+h < row_col:
            if maze[r+h][c] == 0:
                DFS(r+h, c)
            elif maze[r+h][c] == 3:
                result = 1
    for t in tb:
        if c+t >= 0 and c+t < row_col:
            if maze[r][c+t] == 0:
                DFS(r, c+t)
            elif maze[r][c+t] == 3:
                result = 1
#-------------------------------
import sys
sys.stdin = open('sample_maze.txt', 'r')

N = int(input())
for i in range(1, N+1):
    result = 0
    row_col = int(input())
    maze = [list(map(int, input())) for _ in range(row_col)]
    for j in range(len(maze)):
        if 2 in maze[j]:
            a = j
            c = maze[j].index(2)
            break
    for k in range(2):
        DFS(a, c)

    print('#{} {}'.format(i, result))


            
