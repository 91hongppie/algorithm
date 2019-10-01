import sys
sys.stdin = open('hacking.txt', 'r')
from collections import deque
def BFS(num, cnt):
    h = 0
    while Q:
        j = Q.popleft()
        for k in arr[j]:
            h += 1
            Q.append(k)
    arr1[num] = h
    


points, lines = map(int, input().split())
arr = [[] for _ in range(points+1)]
arr1 = []
for _ in range(lines):
    s, e = map(int, input().split())
    arr[e].append(s)
for k in arr:
    arr1.append(len(k))
print(arr1)
# for i in range(points+1):
#     if arr[i]:
#         BFS(i, 0)
a = max(arr1)
po = []
for idx, val in enumerate(arr1):
    if val == a:
        po.append(idx)
print(*po)
