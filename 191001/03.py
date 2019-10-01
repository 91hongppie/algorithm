import sys
sys.stdin = open('03.txt', 'r')
sys.setrecursionlimit(10**8)


def DFS(nums, u, arr):
    global result
    # if result > int(''.join(arr)):
    #     return
    if nums == num:
        q = int(''.join(arr))
        result = max(result, q)
        return
    for i in range(u, len(arr)):
        for j in range(u, len(arr)):
            if i != j:
                if arr[i] <= arr[j]:
                    arr[i], arr[j] = arr[j], arr[i]
                    DFS(nums+1, i, arr)
                    arr[i], arr[j] = arr[j], arr[i]


N = int(input())

for tc in range(1, N+1):
    board, num = map(str, input().split())
    arr = []
    result = 0
    arr.extend(board)
    num = int(num)

    DFS(0, 0, arr)
    print('#{} {}'.format(tc, result))
