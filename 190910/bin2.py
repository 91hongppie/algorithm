import sys; sys.stdin = open('sample_bin2.txt', 'r')

def BIN(num, cnt, result):
    global nums, ans
    if cnt > 13:
        return
    if num == nums:
        ans = result
        return
    BIN(num+1/2**cnt, cnt+1, result+'1')
    BIN(num, cnt+1, result+'0')


N = int(input())

for tc in range(1, N+1):
    nums = float(input())
    i, j  = 1, 1
    result = ''
    ans = ''
    if nums == 0:
        print('#{} 0'.format(tc))
        continue
    BIN(0, 1, result)
    if ans:
        print('#{} {}'.format(tc, ans))
    else:
        print('#{} overflow'.format(tc))