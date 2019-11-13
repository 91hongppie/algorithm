import sys
sys.stdin = open('hacking.txt', 'r')
from collections import deque

def DFS(num):
    global result
    if dp[num]:
        result += dp[num]
        return
    Q.append(num)
    for k in arr[num]:
        a = Q.popleft()
        for k in arr[a]:
            if dp[k]:
                result += dp[k]
            else:
                Q.append(k)
    result += arr1[num]
    dp[num] = result



points, lines = map(int, input().split())
arr = [[] for _ in range(points+1)]
dp = [0 for _ in range(points+1)]
arr1 = []
Q = deque()
for _ in range(lines):
    s, e = map(int, input().split())
    arr[e].append(s)
for k in arr:
    arr1.append(len(k))
for i in range(points+1):
    result = 0
    if arr[i]:
        DFS(i)
a = max(arr1)
po = []
for idx, val in enumerate(arr1):
    if val == a:
        po.append(idx)
a = max(dp)
b = []
for k in range(len(dp)):
    if dp[k] == a:
        b.append(k)
print(*b)
