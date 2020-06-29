import sys
sys.stdin = open('nm.txt', 'r')

def makenm(sn, nm_list):
    if len(nm_list) == length:
        print(*nm_list)
    for u in range(1, nums+1):
        if visit[u] == False:
            visit[u] = True 
            nm_list.append(u)
            makenm(u, nm_list)
            visit[u] = False
            nm_list.pop()

        

nums, length = map(int, input().split())

nums_list = []
visit = [False for _ in range(nums+1)]
for num in range(1, nums+1):
    num_list = [num]
    visit[num] = True
    makenm(num, num_list)
    visit[num] = False
