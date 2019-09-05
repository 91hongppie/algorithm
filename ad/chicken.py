import sys
sys.stdin = open('chicken.txt', 'r')
from queue import Queue

def BFS(r, c, count, area):
    room = list(area)
    print(room)
    x = [1, -1, 0, 0]
    y = [0, 0, -1, 1]
    Q = Queue()
    Q.put([r, c, 0])
    distance = 0
    v = 0
    while Q:
        a = Q.get()
        for ho in range(4):
            if 0 <= a[0]+x[ho] < rc and 0 <= a[1]+y[ho] < rc and room[a[0]+x[ho]][a[1]+y[ho]] != 1:
                Q.put([a[0]+x[ho], a[1]+y[ho], a[2]+1])
            elif 0 <= a[0]+x[ho] < rc and 0 <= a[1]+y[ho] < rc and room[a[0]+x[ho]][a[1]+y[ho]] == 1:
                room[a[0]+x[ho]][a[1]+y[ho]] = 2
                distance += a[2]+1
                v += 1
                if v == count:
                    print(distance)
                    return


            


rc, chicken = map(int, input().split())
area = []
c = 0
for i in range(rc):
    a = list(map(int, input().split()))
    c += a.count(1)
    area.append(a)
for j in range(len(area)):
    for k in range(len(area)):
        if area[j][k] == 2:
            print(area)
            BFS(j, k, c, area)