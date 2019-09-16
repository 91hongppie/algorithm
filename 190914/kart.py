import sys; sys.stdin = open('sample_kart.txt', 'r')
from collections import deque
import itertools 
N = int(input())

for tc in range(1, N+1):
    rc = int(input())
    per_list = deque()
    board = [list(map(int, input().split())) for _ in range(rc)]
    num_list= []
    result1 = 1e9
    for k in range(2, rc+1):
        num_list.append(k)
    for nu in itertools.permutations(num_list):
        kk = deque(nu)
        kk.appendleft(1)
        kk.append(1)
        per_list.append(kk)
    for i in range(len(per_list)):
        you = per_list.pop()
        result = 0
        for h in range(len(you)-1):
            result += board[you[h]-1][you[h+1]-1]
            if result > result1:
                break
        result1 = min(result, result1)  
    print('#{} {}'.format(tc, result1))
