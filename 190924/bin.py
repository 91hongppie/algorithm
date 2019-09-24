import sys
sys.stdin = open('sample_bin.txt', 'r')


def bina(s, e, num, x):
    global cnt
    mid = (s+e) // 2
    if num == a_list[mid]:
        if '11' not in x and '22' not in x:
            cnt += 1
            return
    if e - s <= 1:
        if num != a_list[s] and a_list[e] != num:
            return
        else:
            if num == a_list[e]:
                x += '2'
            if '11' not in x and '22' not in x:
                cnt += 1
            return
    if num > a_list[mid]:
        x += '2'
        bina(mid+1, e, num, x)
    elif num < a_list[mid]:
        x += '1'
        bina(s, mid-1, num, x)


N = int(input())
for tc in range(1, N+1):
    a, b = map(int, input().split())
    a_list = list(map(int, input().split()))
    b_list = list(map(int, input().split()))
    a_list.sort()
    cnt = 0
    for k in b_list:
        x = ''
        bina(0, len(a_list)-1, k, x)
    print('#{} {}'.format(tc, cnt))
