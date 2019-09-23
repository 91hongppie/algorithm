

import sys
sys.stdin = open('sample_input.txt', 'r')


def mergeSort(lo, hi, arr, tmp):  # 매개변수 -> 문제의 크기
    global cnt
    # print(lo, hi)
    if lo == hi:
        return
    # 분할
    mid = (lo + hi) >> 1
    mergeSort(lo, mid, arr, tmp)  # 왼쪽
    mergeSort(mid+1, hi, arr, tmp)  # 오른쪽
    # 왼쪽과 오른쪽 병합
    i, j, k = lo, mid+1, lo
    while i <= mid and j <= hi:  # i는 mid까지 j는 hi 까지 간다
        if arr[i] <= arr[j]:
            tmp[k] = arr[i]
            i, k = i + 1, k + 1
        else:
            tmp[k] = arr[j]
            j, k = j + 1, k + 1

    # if arr[mid] < arr[hi]:
    #     cnt += 1
    while i <= mid:
        tmp[k] = arr[i]
        i, k = i + 1, k + 1
    while j <= hi:
        tmp[k] = arr[j]
        j, k = j + 1, k + 1
    if arr[i-1] > arr[j-1]:
        cnt += 1
    for i in range(lo, hi + 1):
        arr[i] = tmp[i]


N = int(input())
for tc in range(1, N+1):
    nums = int(input())
    arr = list(map(int, input().split()))
    cnt = 0
    tmp = [0] * nums
    mergeSort(0, len(arr)-1, arr, tmp)
    print('#{} {} {}'.format(tc, arr[nums//2], cnt))
