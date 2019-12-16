import sys
sys.stdin = open('circle.txt', 'r')
from collections import deque



row, col, rotation = map(int, input().split())
circles = deque()
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
for _ in range(row):
    circles.append(deque(map(int, input().split())))
for _ in range(rotation):
    x, d, k = map(int, input().split())
    for u in range(x-1, row, x):
        if d == 1:
            circles[u].rotate(-k)
        elif d == 0:
            circles[u].rotate(k)
    x_list = set()
    for r in range(row):
        for c in range(col):
            if circles[r][c] != 0:
                for n in range(4):
                    x = r + dx[n]
                    y = c + dy[n]
                    if 0 <= x < row and y < col:
                        if circles[r][c] == circles[x][y]:
                            x_list.add((r, c,))
                            x_list.add((x, y,))
    if len(x_list) != 0:
        for k in x_list:
            circles[k[0]][k[1]] = 0
    else:
        a = 0
        b = 0
        for ro in range(row):
            a += sum(circles[ro])
            b += col - circles[ro].count(0)
        if a != 0 and b > 1:
            for x1 in range(row):
                for y1 in range(col):
                    if circles[x1][y1] != 0:
                        if circles[x1][y1] > a/b:
                            circles[x1][y1] -= 1
                        elif circles[x1][y1] < a/b:
                            circles[x1][y1] += 1

    c = 0
    for q in circles:
        c += sum(q)
print(c)