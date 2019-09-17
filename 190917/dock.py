import sys
sys.stdin = open('input_dock.txt', 'r')

N = int(input())

for tc in range(1, N+1):
    nums = int(input())
    cars = []
    for _ in range(nums):
        cars.append(list(map(int, input().split())))
    result = []
    for i in range(1 << len(cars)):
        a = []
        for n in range(len(cars)):
            if i & (1 << n):
                a.append(cars[n])
        if a:
            result.append(a)
    print(result)
