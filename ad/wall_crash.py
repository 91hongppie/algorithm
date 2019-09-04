import sys
sys.stdin = open('wall_crash.txt', 'r')

row, col = map(int, input().split())
room = [[] for _ in range(row)]
for i in range(row):
    a = list(input())
    room[i].extend(a)

