import sys
sys.stdin  = open("sample_input.txt", "r")
num = int(input())
for k in range(1, num+1):
    arr_2 = map(int, input().split())
    arr = list(map(int, input().split()))
    total = 0
    result = 0

    for j in range(0, len(arr)-1):
        for i in range (0, len(arr)-1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
            else:
                continue
    total = arr[len(arr)-1] - arr[0]
    print('#{} {}'.format(k, total))