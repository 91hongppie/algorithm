import sys
sys.stdin = open('NnM1.txt', 'r')

    
def comb(e, n):
    global result
    if n == nums:
        q = sorted(result)
        if q not in a:
            a.append(q)
            print(*q)
        return
    else:
        for i in range(1, num+1):
            result.append(i)
            comb(e+1, n+1)
            result.pop()


num, nums = map(int, input().split())
a = []
result = []
comb(0, 0)


