import sys
sys.stdin = open('input_russia.txt', 'r')

N = int(input())

for tc in range(1, N+1):
    r, c = map(int, input().split())
    flag = []
    for _ in range(r):
        flag.append(list(map(str, input())))
    a = 0
    W = B = R = 0
    j = 1
    result1 = 1e9
    while j != len(flag)-1:
        l = j
        while l != len(flag):
            result = 0
            for k in range(0, j):
                result += c - flag[k].count('W')
            for q in range(j, l):
                result += c - flag[q].count('B')
            for y in range(l, len(flag)):
                result += c - flag[y].count('R')
            l += 1
            result1 = min(result1, result)
        j += 1
    print('#{} {}'.format(tc, result1))

