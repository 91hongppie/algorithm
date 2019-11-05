import sys
from pprint import pprint
sys.stdin = open('sail.txt', 'r')

def BFS(num):
    global a, node_list
    dx = [-1, -1, -1, 1, 1, 1, 0, 0]
    dy = [0 ,-1, 1, -1, 1, 0, 1, -1]
    for i in range(1, row-1):
        for j in range(1, col-1):
            if board[i][j] == '.' or board[i][j] == 9:
                continue
            else:
                b = 0
                for k in range(8):
                    x = i + dx[k]
                    y = j + dy[k]
                    if 0 <= x < row and 0 <= y < col:
                        if board[x][y] == '.':
                            b += 1
                        if b >= int(board[i][j]):
                            a += 1
                            node_list.append([i, j])
                            break



