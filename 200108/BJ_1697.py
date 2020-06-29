import sys
sys.stdin = open('BJ_1697.txt', 'r')
from collections import deque

def BFS(s_p, e_p):
    Q.append({s_p, 0})
    visit[s_p] = 0
    while Q:
        s, t = Q.popleft()
        print(s, t)
        if s == e_p:
            print(t)
            return
        if s+1 <= e_p and visit[s+1] > t+1:
            Q.append({s+1, t+1})
        if 2*s <= e_p + 1 and visit[2*s] > t+1:
            Q.append({2*s, t+1})
        if s-1 >= 0 and visit[s-1] > t+1:
            Q.append({s-1, t+1})

old, young = map(int, input().split())
Q = deque()
visit = [100] * 100001
BFS(old, young)