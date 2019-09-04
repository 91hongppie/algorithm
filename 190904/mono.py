import sys
sys.stdin = open('input_mono.txt', 'r')
from itertools import combinations

N = int(input())

for u in range(1, N+1):
    nums = int(input())
    result = []
    for nums in combinations(list(map(int, input().split())), 2):
        result.append(str(nums[0]*nums[1]))
    a = []
    d = 0
    for k in result:
        if len(k) > 1:
            c = k[0]
            for y in range(1, len(k)):
                if c <= k[y]:
                    c = k[y]
                    d = 1
                else:
                    d = 0
                    break
            if d == 1:
                a.append(int(k))
    if len(a) == 0:
        print('#{} -1'.format(u))
    else:
        print('#{} {}'.format(u, max(a)))