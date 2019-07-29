import sys
sys.stdin  = open("input.txt", "r")

for k in range(1, 11):
    N = int(input())
    arr = list(map(int, input().split()))
    total = 0


    for i in range(2, len(arr)-2):
        if arr[i-1]<arr[i] and arr[i+1]<arr[i] and arr[i-2]<arr[i] and arr[i+2]<arr[i]:
            max_floor = 0
            for j in range(0, 5):
                if j == 0:
                    max_floor = arr[i-2]
                elif max_floor < arr[i-2+j] and j != 2:
                    max_floor = arr[i-2+j]
            total += arr[i] - max_floor
    print('#{} {}'.format(k, total))


