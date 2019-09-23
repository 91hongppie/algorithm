import sys
sys.stdin = open('input_russia.txt', 'r')
N = int(input())

for tc in range(1, N+1):
    r, c = map(int, input().split())
    flag = []
    for _ in range(r):
        flag.append(list(map(str, input())))
    print(flag)
