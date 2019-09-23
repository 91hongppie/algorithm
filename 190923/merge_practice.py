import sys
sys.stdin = open('sample_input.txt', 'r')


def merge(arr):
    global cnt
    if len(arr) == 1:
        return
    mid = len(arr) // 2
    g1 = arr[:mid]
    g2 = arr[mid:]
    merge(g1)
    merge(g2)
    if g1[-1] > g2[-1]:
        cnt += 1
    i1 = i2 = ia = 0
    while i1 < len(g1) and i2 < len(g2):
        if g1[i1] > g2[i2]:
            arr[ia] = g2[i2]
            ia += 1
            i2 += 1
        else:
            arr[ia] = g1[i1]
            ia += 1
            i1 += 1
    while i1 < len(g1):
        arr[ia] = g1[i1]
        i1 += 1
        ia += 1
    while i2 < len(g2):
        arr[ia] = g2[i2]
        i2 += 1
        ia += 1

N = int(input())
for tc in range(1, N+1):
    nums = int(input())
    arr = list(map(int, input().split()))
    cnt = 0
    merge(arr)
    print('#{} {} {}'.format(tc, arr[len(arr)//2], cnt))
