import sys
sys.stdin = open('03.txt', 'r')
sys.setrecursionlimit(10**8)


def dfs(n, su):
    global co, result
    if su != '' and eval(su) == result:
        co.append(len(su))
        return
    elif su != '' and eval(su) > result:
        return
    for i in nums:
        dfs(n-1, su+i)
        if result // eval(su) > 10:
            dfs(n-1, su+'*'+i)


N = int(input())

for tc in range(1, N+1):
    co = []
    num_list = list(map(int, input().split()))
    nums = []
    result = int(input())
    for i in range(len(num_list)):
        if num_list[i] == 1:
            nums.append(str(i))
    for j in nums:
        dfs(len(nums)-1, j)
    print(min(co)+1)
