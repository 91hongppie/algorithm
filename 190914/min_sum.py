from collections import deque
import sys
sys.stdin = open('sample_min_sum.txt', 'r')


def BFS(r, c, cnt):
    global distance
    Q.append([r, c, cnt])
    while Q:
        a, b, c = Q.popleft()
        dr = [0, 1]
        dd = [1, 0]
        for ku in range(2):
            a1 = a + dr[ku]
            b1 = b + dd[ku]
            if a1 < rc and b1 < rc:
                if distance[a1][b1] == 0:
                    distance[a1][b1] = c + room[a1][b1]
                    Q.append([a1, b1, c+room[a1][b1]])
                elif distance[a1][b1] > c + room[a1][b1]:
                    distance[a1][b1] = c + room[a1][b1]
                    Q.append([a1, b1, c+room[a1][b1]])
                else:
                    continue


N = int(input())

for tc in range(1, N+1):
    Q = deque()
    rc = int(input())
    room = [list(map(int, input().split())) for _ in range(rc)]
    distance = [[0]*rc for _ in range(rc)]
    BFS(0, 0, room[0][0])
    print(distance)
    print('#{} {}'.format(tc, distance[rc-1][rc-1]))
