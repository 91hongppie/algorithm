import sys
sys.stdin = open('sample_수열편집.txt', 'r')

N = int(input())

for i in range(1, N+1):
    length, nums, index = map(int, input().split())
    nums_list = list(map(int, input().split()))
    for k in range(nums):
        mod_list = list(input().split())
        if mod_list[0] == 'I':
            nums_list.insert(int(mod_list[1]), int(mod_list[2]))
        elif mod_list[0] == 'D':
            nums_list.pop(int(mod_list[1]))
        elif mod_list[0] == 'C':
            nums_list[int(mod_list[1])] = int(mod_list[2])
    if len(nums_list) <= index:
        print('#{} -1'.format(i))
    else:
        print('#{} {}'.format(i, nums_list[index]))