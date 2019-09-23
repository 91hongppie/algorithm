import sys
sys.stdin = open('NnM1.txt', 'r')

def comb(e, n):
    global result
    if n == nums:
        print(*result)
        return
    else:
        for i in range(1, num+1):
            if not visit[i]:
                visit[i] = True
                result.append(i)
                comb(e+1, n+1)
                visit[i] = False
                result.pop()

    
num, nums = map(int, input().split())
a = []
result = []
visit = [False for _ in range(num+1)]
comb(1, 0)
