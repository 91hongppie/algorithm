import sys
sys.stdin = open('input_sample.txt', 'r')

N = int(input())
area_list = [[0]*101 for _ in range(101)]
for i in range(1, N+1):
    area = list(map(int, input().split()))
    for k in range(area[0], area[0]+area[2]):
        for h in range(area[1], area[1]+area[3]):
            area_list[k][h] += 1
j = 1
while j < N+1:
    i = 0
    result = 0
    while i < 101:
        result += area_list[i].count(j)
        i += 1
    j += 1
    if result == 0:
        print(0)
    else:
        print(result)
    
