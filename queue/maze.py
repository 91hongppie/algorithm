def DFS(r, c, n, stack):
    n += 1
    tb = [-1, +1]
    maze[r][c] = 1
    for h in tb:
        if r+h >= 0 and r+h < row_col:
            if maze[r+h][c] == 0:
                stack.append(0)
                DFS(r+h, c, n, stack)
                
            elif maze[r+h][c] == 3:
                stack.append(3)
                print('#{} {}'.format(i, n-1))
        if c+h >= 0 and c+h < row_col:
            if maze[r][c+h] == 0:
                stack.append(0)
                DFS(r, c+h, n, stack)
            elif maze[r][c+h] == 3:
                stack.append(3)
                print('#{} {}'.format(i, n-1))
                
#-----------------------------------------------------------------------
import sys
sys.stdin = open('sample_maze.txt', 'r')
N = int(input())
for i in range(1, N+1):
    row_col = int(input())
    stack = []
    result = 0
    maze = [list(map(int, input())) for _ in range(row_col)]
    for j in range(len(maze)):
        if 2 in maze[j]:
            a = j
            c = maze[j].index(2)
            break
    num = 0
    a = DFS(a, c, num, stack)
    if not sum(stack):
        print('#{} 0'.format(i))
