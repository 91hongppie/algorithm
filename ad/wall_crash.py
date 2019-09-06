import sys
sys.stdin = open('wall_crash.txt', 'r')
from collections import deque

def BFS(s, e, cnt):


row, col = map(int, input().split())
room = [list(map(int, input())) for _ in range(row)]
visit = [[False]*col for _ in range(row)]
Q = deque()
BFS(0, 0, 1)
