def BFS(idx, cnt):
    global ans
    if idx > len(chicken):
        return
    if cnt == m:
        s = 0
        for hx, hy in home:
            d = 1000000000
            for k in v:
                cx, cy = chicken[k]
                d = min(d, abs(hx-cx)+abs(hy-cy))
            s += d
        ans = min(ans,s)
        return
    v.append(idx)
    BFS(idx+1, cnt+1)
    v.pop()
    BFS(idx+1, cnt)      
        
import sys
sys.stdin = open('chicken.txt', 'r')

rc, m = map(int, input().split())
area = []
for i in range(rc):
    a = list(map(int, input().split()))

chicken, home, v = [], [], [] 
for j in range(len(area)):
    for k in range(len(area)):
        if area[j][k] == 2:
            chicken.append([j, k])
        elif area[j][k] == 1:
            home.append([j, k])
ans = 10000000000
BFS(0, 0)
print(ans)