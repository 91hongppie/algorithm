import sys
sys.stdin = open('sisters.txt', 'r')
from collections import deque
def BFS(o, y):
    global result
    Q.append([o, 0])
    while Q:
        a, nums = Q.popleft()
        if a == y:
            result = nums
            return
        Q.append([a*2, nums+1])
        Q.append([a+1, nums+1])
        Q.append([a-1, nums+1])


Q = deque()
old, young = map(int, input().split())
result = 0
BFS(old, young)
print(result)