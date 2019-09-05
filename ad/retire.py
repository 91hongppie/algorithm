import sys
sys.stdin = open('retire.txt', 'r')

def DFS(day, a, money, result):
    if day+a > N:
        m = money-cal[day][1]
        result.append(m)
        return
    elif day+a == N:
        result.append(money)
    elif day+a < N:
        for k in range(day+a, N):
            DFS(k, cal[k][0], money+cal[k][1], result)
            


N = int(input())
cal = []
result = []
for i in range(N):
    cal.append(list(map(int, input().split())))

for idx, j in enumerate(cal):
    DFS(idx, cal[idx][0], cal[idx][1], result)
print(max(result))