import sys
sys.stdin = open('sample_input.txt', 'r')

P = [i for i in range(1, 13)]
n = len(P)
result = []
N = int(input())
for i in range(1<<n):
    a = []
    for j in range(n):
        if i & (1<<j):
            a.append(P[j])
    result.append(a)
for k in range(1, N+1):
    num, a_sum = map(int, input().split())
    count = 0
    for l in result:
        if len(l) == num and sum(l) == a_sum:
            count += 1
    print('#{} {}'.format(k, count))