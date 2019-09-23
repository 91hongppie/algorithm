import sys
sys.stdin = open('NnM1.txt', 'r')

num, nums = map(int, input().split())
a = []
result = []
visit = [False for _ in range(num+1)]
num_list = [i for i in range(1, num+1)]
i = 1<<len(num_list)
j = len(num_list)
result = []
for k in range(1, i+1):
    a = []
    for y in range(j):
        if k & (1<<y):
            a.append(num_list[y])
    if len(a) == nums:
        result.append(a)
result.sort()
for z in result:
    print(*z)
