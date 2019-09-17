import sys
sys.stdin = open('input_container.txt', 'r')

N = int(input())

for tc in range(1, N+1):
    container, truck = map(int, input().split())
    containers = list(map(int, input().split()))
    trucks = list(map(int, input().split()))
    containers.sort()
    trucks.sort()
    result = 0
    for k in range(len(trucks)):
        for y in range(len(containers)-1, -1, -1):
            if trucks[k] >= containers[y]:
                result += containers[y]
                containers[y] = 101
                break

    print('#{} {}'.format(tc, result))
