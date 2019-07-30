import sys
sys.stdin  = open("sample_input_02.txt", "r")
num = int(input())
for k in range(1, num+1):
    arr_2 = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    total = 0
    result = 0
    terminal = []
    charger = []


    fuel = arr_2[0]
    count = 0
    for idx, val in enumerate(charger):
        if charger[idx] == 0:
            fuel -= 1
            continue
        if charger[idx] == 1 :
            arr(idx)

            count += 1
        if arr[u-1] - arr[u-2] <= fuel < arr[u]-arr[u-2]:
            count += 1
            continue
        else:
            count = 0
            break
    print('# {} {}'.format(k, count))