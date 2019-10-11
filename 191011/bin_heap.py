import sys
sys.stdin = open('bin_heap.txt', 'r')


N = int(input())
for tc in range(1, N+1):
    nodes = int(input())
    nums = list(map(int, input().split()))
    child = [[0, 0] for _ in range(nodes+1)]
    result = [0 for _ in range(nodes+1)]
    cnt = 0
    for i in range(1, nodes+1):
        if 2 * i <= nodes:
            child[i][0] = 2 * i
        if 2 * i + 1 <= nodes:
            child[i][1] = 2 * i + 1
    for k in range(nodes+1):
        result[k] = nums[k-1]
        if k > 1:
            j = k
            while j // 2 > 0:
                if result[j//2] > result[j]:
                    result[j], result[j//2] = result[j//2], result[j]
                j = j // 2
    i = nodes
    k = 0
    while i != 1:
        i = i//2
        k += result[i]
    print('#{} {}'.format(tc, k))
