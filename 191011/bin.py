import sys
sys.stdin = open('bin.txt', 'r')


def inorder(n):
    global result, cnt
    if n != 0:
        inorder(child[n][0])
        result[n] = cnt
        cnt += 1
        inorder(child[n][1])


N = int(input())

for tc in range(1, N+1):
    cnt = 1
    nums = int(input())
    child = [[0, 0] for _ in range(nums+1)]
    result = [0 for _ in range(nums+1)]
    for i in range(1, nums+1):
        if 2 * i <= nums:
            child[i][0] = 2 * i
        if 2 * i + 1 <= nums:
            child[i][1] = 2 * i + 1
    inorder(1)
    print('#{} {} {}'.format(tc, result[1], result[nums//2]))
