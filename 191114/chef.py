import sys
sys.stdin = open('chef.txt', 'r')
from itertools import combinations

N = int(input())
for tc in range(1, N+1):
    rc = int(input())
    board = [list(map(int, input().split())) for _ in range(rc)]
    visit = [False for _ in range(rc)]
    result = 1e9
    scores = [[0]*rc for _ in range(rc)]
    for u in range(rc):
        for y in range(u, rc):
            scores[u][y] = board[u][y] + board[y][u]
    result =1e9
    a = combinations(range(rc), rc//2)
    list_a = list(a)
    for j in range(len(list_a)):
        cook_list_a = set(list_a[j])
        cook_list_b = list(set(range(rc))-cook_list_a)
        cook_list_a = list(cook_list_a)
        s_1 = 0
        s_2 = 0
        for g in range(len(cook_list_a)):
            for w in range(g, len(cook_list_a)):
                s_1 += scores[cook_list_a[g]][cook_list_a[w]]
                s_2 += scores[cook_list_b[g]][cook_list_b[w]]
        s_2 = abs(s_1-s_2)
        if result > s_2:
            result = s_2
    print('#{} {}'.format(tc, result))
            
