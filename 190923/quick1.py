arr = [69, 10, 30, 2, 16, 8, 31, 22]


def quickSort(lo, hi, arr):
    if lo >= hi:
        return
    i = lo - 1
    for j in range(lo, hi):
        if arr[hi] >= arr[j]:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    i += 1
    arr[hi], arr[i] = arr[i], arr[hi]

    quickSort(lo, i-1, arr)
    quickSort(i+1, hi, arr)


print(arr)
quickSort(0, len(arr)-1, arr)
print(arr)
