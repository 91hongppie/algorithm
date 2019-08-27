def division(f, l):
    if f == l:
        return f
    le = division(f, (f+l)//2)
    ri = division((f+l)//2+1, l)
    return winner(le, ri)

    

def winner(le, ri):
    if team[le-1] == 1 and team[ri-1] == 3:
        return le
    elif team[le-1] == 2 and team[ri-1] == 1:
        return le
    elif team[le-1] == 3 and team[ri-1] == 2:
        return le
    elif team[le-1] == team[ri-1]:
        return le
    else:
        return ri

import sys
sys.stdin = open('sample_tournament.txt', 'r')

N = int(input())
for i in range(1, N+1):
    n = int(input())
    team = list(map(int, input().split()))
    s = 1
    e = len(team)
    print('#{} {}'.format(i, division(s, e)))
   
    

