import sys; sys.stdin = open('input_container.txt', 'r')
from collections import deque
N = int(input())

for tc in range(1, N+1):
    container, truck = map(int, input().split())
    containers = list(map(int, input().split()))
    trucks = list(map(int, input().split()))
    containers.sort()
    trucks.sort()
    print(trucks, containers)
    