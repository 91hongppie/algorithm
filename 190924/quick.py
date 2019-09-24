import sys
sys.stdin = open('sample_quick.txt', 'r')


def quickSort(lo, hi):
    if lo >= hi:
        return
    i = lo - 1
    for j in range(lo, hi):  # 시작위치 ~ 마지막 전까지..
        if arr[hi] >= arr[j]:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    i += 1
    arr[hi], arr[i] = arr[i], arr[hi]  # i 다음 위치 애랑 pivot 바꾸기

    quickSort(lo, i - 1)
    quickSort(i + 1, hi)


N = int(input())

for tc in range(1, N+1):
    leng = int(input())
    arr = list(map(int, input().split()))
    quickSort(0, len(arr) - 1)
    print('#{} {}'.format(tc, arr[leng//2]))
