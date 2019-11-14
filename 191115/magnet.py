import sys
sys.stdin = open('magnet.txt', 'r')

def DFS(n, d):
    global result 
    for k in range(n-1, 3):
        if magnets[k][2] != magnets[k+1][6]:
            if abs(k + 2 - n) % 2:
                if d == 1:
                    re_clock.append(k+2)
                else:
                    clock.append(k+2)
            else:
                if d == 1:
                    clock.append(k+2)
                else:
                    re_clock.append(k+2)
        else:
            break
    for u in range(n-1, 0, -1):
        if magnets[u][6] != magnets[u-1][2]:
            if abs(u-n) % 2:
                if d == 1:
                    re_clock.append(u)
                else:
                    clock.append(u)
            else:
                if d == 1:
                    clock.append(u)
                else:
                    re_clock.append(u)
        else:
            break


N = int(input())

for tc in range(1, N+1):
    nums = int(input())
    magnets = [list(map(int, input().split())) for _ in range(4)]
    for i in range(nums):
        num, direction = map(int, input().split())
        if direction == 1:
            clock = [num]
            re_clock = []
        else:
            clock = []
            re_clock = [num]
        DFS(num, direction)
        for k in clock:
            for u in range(7, 0, -1):
                magnets[k-1][u], magnets[k-1][u-1] = magnets[k-1][u-1], magnets[k-1][u]
        for y in re_clock:
            a = magnets[y-1].pop(0)
            magnets[y-1].append(a)
    result = 0
    for k in range(4):
        if magnets[k][0] == 1:
            if k  == 0:
                result += 1
            elif k == 1:
                result += 2
            elif k == 2:
                result += 4
            elif k == 3:
                result += 8
    print('#{} {}'.format(tc, result))
