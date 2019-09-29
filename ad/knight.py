import sys
sys.stdin = open('knight.txt', 'r')
from collections import deque

def knight(r, c, cnt):
    global result
    Q.append([r, c, cnt])
    while Q:
        a, b, c = Q.popleft()
        dx = [2, 2, -2, -2, 1, 1, -1, -1]
        dy = [1, -1, 1, -1, 2, -2, 2, -2]
        if a == e_point[0] and b == e_point[1]:
            print(c)
            return
        for i in range(8):
            x = a + dx[i]
            y = b + dy[i]
            Q.append([x, y, c+1])


N = int(input())

for tc in range(1, N+1):
    result = 1e9
    Q = deque()
    rc = int(input())
    s_point = list(map(int, input().split()))
    e_point = list(map(int, input().split()))
    knight(s_point[0], s_point[1], 0)
