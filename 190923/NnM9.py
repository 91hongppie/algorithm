import sys
sys.stdin = open('NnM9.txt', 'r')


def perm(s, re):
    if len(re) == leng:
        print(*re)
    else:
        if s < len(num_list)-1:
            re.append(num_list[s])
            perm(s+1, re)
            re.pop()
            perm(s+1, re)


nums, leng = map(int, input().split())
num_list = list(map(int, input().split()))
num_list.sort()
re = []
for i in range(nums):
    perm(i, re)
