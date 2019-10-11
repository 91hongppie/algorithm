import sys
sys.stdin = open('subtree.txt', 'r')


def preorder(n):
    global count
    if n != 0:
        count += 1
        preorder(child[n][0])
        preorder(child[n][1])


N = int(input())

for tc in range(1, N+1):
    E, N = map(int, input().split())
    arr = list(map(int, input().split()))
    child = [[0, 0] for _ in range(E+2)]
    for k in range(0, len(arr), 2):
        if child[arr[k]][0] == 0:
            child[arr[k]][0] = arr[k+1]
        else:
            child[arr[k]][1] = arr[k+1]
    count = 0
    preorder(N)
    print('#{} {}'.format(tc, count))
