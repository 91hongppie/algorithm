import sys
sys.stdin = open('calcul.txt', 'r')

N = int(input())
for tc in range(1, N+1):
    nums = list(map(int, input().split()))
    result = []
    for index, num in enumerate(nums):
        if num == 1:
            result.append(str(index))
    result_num = int(input())
    answer = ''
    num = 0
    
    
