import sys
sys.stdin = open('sum_node.txt', 'r')

N = int(input())

for tc in range(1, N+1):
    nodes, leaf, result_node = map(int, input().split())
    child = [0 for _ in range(nodes+1)]
    for _ in range(leaf):
        n, e = map(int, input().split())
        child[n] = e
    for i in range(nodes, 0, -1):
        if i % 2 == 0:
            if i == nodes:
                child[i//2] = child[i]
            else:
                child[i//2] = child[i] + child[i+1]
    print('#{} {}'.format(tc, child[result_node]))
