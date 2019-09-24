import sys
sys.stdin = open('hide_n_seek.txt', 'r')


def hide(b, s, cnt):
    global result
    if cnt >= result:
        return
    if b == s:
        result = min(result, cnt)
    elif b < s:
        hide(b+2*cnt+1, s, cnt+1)
        hide(b+1, s, cnt+1)
    elif b > s:
        hide(b-1, s, cnt+1)


subin, sister = map(int, input().split())
result = 1e9
hide(subin, sister, 0)
print(result)
