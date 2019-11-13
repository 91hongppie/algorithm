import sys
sys.stdin = open('nums.txt', 'r')
import math 

def cal(num, oper, result_int):
    global result, max_value, min_value
    if num == nums-1:
        max_value = max(max_value, result_int)
        min_value = min(min_value, result_int)
        return
    for k in range(4):
        if oper[k] > 0:
            oper[k] -= 1
            if k == 0:
                result_int += numbers[num+1]
                cal(num+1, oper, math.trunc(result_int))
                result_int -= numbers[num+1]
            elif k == 1:
                result_int -= numbers[num+1]
                cal(num+1, oper, math.trunc(result_int))
                result_int += numbers[num+1]
            elif k == 2:
                result_int *= numbers[num+1]
                cal(num+1, oper, math.trunc(result_int))
                result_int /= numbers[num+1]
            elif k == 3:
                result_int /= numbers[num+1]
                cal(num+1, oper, math.trunc(result_int))
                result_int *= numbers[num+1]
            oper[k] += 1



N = int(input())

for tc in range(1, N+1):
    result = []
    nums = int(input())
    opers = list(map(int, input().split()))
    numbers = list(map(int, input().split()))
    result = []
    max_value = -1e9
    min_value = 1e9
    cal(0, opers, numbers[0])
    print('#{} {}'.format(tc, max_value-min_value))