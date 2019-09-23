import sys 
sys.stdin = open('NnM1.txt', 'r')


N, M = map(int, input().split())
choose = []

def perm(k, s):
    if k == M:
        print(*choose)
        return
    for i in range(s, N + 1):
        if len(choose) == 0:
            choose.append(i)
            perm(k + 1, s)
            choose.pop()
        elif i >= choose[-1]:
            choose.append(i)
            perm(k + 1, s)
            choose.pop()
perm(0, 1)