import sys
sys.stdin = open('sample_list_sum.txt', 'r')
import itertools

N = int(input())

for i in range(1, N+1):
    rc = int(input())
    sum_list = []
    for j in range(rc):
        sum_list.append(list(map(int, input().split())))
    a = [0] * (len(sum_list)+1)
    per_list = []
    for k in range(1, len(sum_list)+1):
        per_list.append(k)
    a = []
    result = []
    for p in itertools.permutations(per_list):
        a.append(list(p))
    for t in a:
        r= [0]
        for h in range(len(t)):
            r[0] += sum_list[h][t[h]-1]
        result.append(r[0])
    result = sorted(result)
    print('#{} {}'.format(i, result[0]))
