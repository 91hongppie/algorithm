import sys
sys.stdin = open('NnM1.txt', 'r')

def comb(e, n, result):
    if n == nums:
        print(*result)
        return
    else:
        if e == 1:
            for i in range(1, num+1):
                result.append(i)
                comb(e+1, n+1, result)
                result.pop()
        else:
            for i in range(result[-1], num+1):
                result.append(i)
                comb(e+1, n+1, result)
                result.pop()

    
num, nums = map(int, input().split())
a = []
result = []
comb(1, 0, result)