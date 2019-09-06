import sys
sys.stdin = open('chicken.txt', 'r')

def solve(idx, cnt):
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
    solve(idx+1, cnt+1)
    v.pop()
    solve(idx+1, cnt)      
        
rc, m = map(int, input().split())
area = []
for i in range(rc):
    a = list(map(int, input().split()))
    area.append(a)

chicken, home, v = [], [], [] 
for j in range(rc):
    for k in range(rc):
        if area[j][k] == 2:
            chicken.append([j, k])
        elif area[j][k] == 1:
            home.append([j, k])
ans = 10000000000
solve(0, 0)
print(ans)